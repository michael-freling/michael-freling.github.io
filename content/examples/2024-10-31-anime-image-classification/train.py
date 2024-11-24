# https://huggingface.co/blog/fine-tune-vit

import datasets
import json
import sys
import multiprocessing as mp

datasets_dir = sys.argv[1] if len(sys.argv) >= 2 else './datasets'
output_dir = sys.argv[2] if len(sys.argv) >= 3 else './model'

# https://huggingface.co/docs/datasets/image_load#imagefolder
ds = datasets.load_dataset('imagefolder', data_dir=datasets_dir, num_proc=mp.cpu_count())
with open(f'{datasets_dir}/tags.json', 'r') as f:
    tags = json.loads(f.read())
# print(tags)

from transformers import ViTImageProcessor

# https://huggingface.co/google/vit-base-patch16-224
model_name_or_path = 'google/vit-base-patch16-224-in21k'
processor = ViTImageProcessor.from_pretrained(model_name_or_path)

def transform(batch):
    # The ViTImageProcessor struggles with RGBA images since it typically expects RGB images
    inputs = processor([x.convert("RGB") for x in batch['image']], return_tensors='pt')
    inputs['tags'] = batch['tags']
    return inputs

prepared_ds = ds.with_transform(transform)

# data collator
import torch

def collate_fn(batch):
    return {
        'pixel_values': torch.stack([x['pixel_values'] for x in batch]),
        'labels': torch.tensor([x['tags'] for x in batch]),
    }

## load_metric is deprecated https://discuss.huggingface.co/t/unable-to-import-load-metric/110268/3
import evaluate
import transformers

# metric = evaluate.load("accuracy")
# https://huggingface.co/blog/Valerii-Knowledgator/multi-label-classification
metrics = evaluate.combine(["accuracy", "f1", "precision", "recall"])

# Define an evaluation metric
import numpy as np

def sigmoid(x):
   return 1/(1 + np.exp(-x))

def compute_metrics(p: transformers.EvalPrediction):
    predictions, labels = p
    predictions = sigmoid(predictions)
    predictions = (predictions > 0.5).astype(int).reshape(-1)

    return metrics.compute(predictions=predictions, references=labels.astype(int).reshape(-1))

from transformers import ViTForImageClassification

model = ViTForImageClassification.from_pretrained(
    model_name_or_path,
    # Multi label classification: https://github.com/huggingface/transformers/issues/16003#issuecomment-1062714136
    problem_type="multi_label_classification",
    num_labels=len(tags),
    id2label={str(i): c for i, c in enumerate(tags)},
    label2id={c: str(i) for i, c in enumerate(tags)}
)


from transformers import TrainingArguments

training_args = TrainingArguments(
  output_dir=output_dir,
  fp16=True,
#   save_steps=2,
#   eval_steps=2,
#   logging_steps=1,
#   learning_rate=2e-4,
#   save_total_limit=2,
  remove_unused_columns=False,
#   push_to_hub=False,
#   report_to='tensorboard',

  load_best_model_at_end=True,
  eval_strategy="steps",
  # Data Preloading parameters: https://huggingface.co/docs/transformers/perf_train_gpu_one
  dataloader_num_workers=4,
)

from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=collate_fn,
    compute_metrics=compute_metrics,
    train_dataset=prepared_ds["train"],
    eval_dataset=prepared_ds["validation"],
    tokenizer=processor,
)

## train
train_results = trainer.train()
trainer.save_model()
trainer.log_metrics("train", train_results.metrics)
trainer.save_metrics("train", train_results.metrics)
trainer.save_state()

## Evaluate
metrics = trainer.evaluate(prepared_ds['validation'])
trainer.log_metrics("eval", metrics)
trainer.save_metrics("eval", metrics)
