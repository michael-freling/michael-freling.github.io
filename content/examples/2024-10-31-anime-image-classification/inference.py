from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import torch

processor = ViTImageProcessor.from_pretrained('./trained')
model = ViTForImageClassification.from_pretrained('./trained')

# url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
url = 'https://cdn.nekosia.cat/images/catgirl/66b0128c36c1176963856fd6.jpg'
response = requests.get(url, stream=True)
# print(response.text)
image = Image.open(response.raw).convert("RGB")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = torch.sigmoid(outputs.logits)
# Top 5
# logits = torch.topk(logits, top_k, dim=1).indices.squeeze(0)

# model predicts one of the 1000 ImageNet classes
print(logits)

threshold = 0.5
predicted_indices = (logits > threshold).nonzero(as_tuple=True)[1]
print(predicted_indices)
predicted_labels = [model.config.id2label[idx.item()] for idx in predicted_indices]

print("Predicted class:", predicted_labels)
