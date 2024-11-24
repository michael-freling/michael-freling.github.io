---
title: Build an image classification model for Anime images
date: 2024/10/31
---


Read
https://huggingface.co/blog/fine-tune-vit

- Create a dataset: https://huggingface.co/docs/datasets/use_with_pytorch#datasets.Image

## Pitfalls

- imagefolder: https://huggingface.co/docs/datasets/image_dataset#imagefolder
    - metadata.jsonl
- ds['train].features <- no data?
- The ViTImageProcessor struggles with RGBA images since it typically expects RGB images
- Multi label classification: https://github.com/huggingface/transformers/issues/16003#issuecomment-1062714136
    - Compute metrics: https://huggingface.co/blog/Valerii-Knowledgator/multi-label-classification
- Export tags and images in DigiKam
    - XMP sidecar files:
        - https://docs.digikam.org/en/setup_application/config_overview.html
        - https://docs.digikam.org/en/setup_application/metadata_settings.html
    - Python xmp toolkit: https://python-xmp-toolkit.readthedocs.io/en/latest/installation.html
- Multi processing: https://www.machinelearningplus.com/python/parallel-processing-python/


## Build an image



## Build an image
