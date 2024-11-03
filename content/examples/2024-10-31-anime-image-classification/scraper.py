# https://oxylabs.io/blog/python-web-scraping
import requests
import json
import os
import datasets
import shutil
import torch
from PIL import Image

IMAGE_COUNT=2
SOURCE_DIR='./source'
SOURCE_DIGIKAM_DIR='./source/digikam'
OUTPUT_DIR='./datasets'

from libxmp.utils import file_to_dict

def read_digikam_files(source_dir: str):
    xmp_files = [file for file in os.listdir(source_dir) if file.endswith('.xmp')]

    with open(f'{source_dir}/metadata.jsonl', 'w') as output_file:
        for xmp_file in xmp_files:
            xmp: dict = file_to_dict(f'{source_dir}/{xmp_file}')
            image_file = xmp_file.replace('.xmp', '')

            tags: list[str] = []
            digiKamMetadata: list[tuple[str, str,dict]] = xmp['http://www.digikam.org/ns/1.0/']
            for t in digiKamMetadata:
                dom, value, _ = t
                if not dom.startswith('digiKam:TagsList['):
                    continue
                parts = value.split('/')
                if len(parts) == 3 and parts[2].startswith('Season'):
                    # series season tag: Anime/{Series name}/{Season 1}
                    tags.append(parts[1])
                    tags.append(parts[2])
                    continue
                if len(parts) == 4 and parts[2].startswith('Characters'):
                    # character tag: Anime/{Series name}/Characters/{Character name}
                    tags.append(parts[3])
                    continue
                tags.append(value)

            line = {
                'file_name': image_file,
                'tags': tags
            }
            output_file.write(json.dumps(line) + '\n')

# def download_images():
#     response = requests.get(
#         f'https://api.nekosia.cat/api/v1/images/catgirl?rating=safe&count={IMAGE_COUNT}'
#     )
#     if response.status_code != 200:
#         print('Failed to fetch data ' + str(response.json()))
#         return

#     data = response.json()

#     if not os.path.exists(f'{SOURCE_DIR}'):
#         os.makedirs(f'{SOURCE_DIR}')

#     images = data['images']
#     for index in range(len(images)):
#         id, url, extension = images[index]['id'], images[index]['image']['original']['url'], images[index]['metadata']['original']['extension']
#         image_response = requests.get(url)
#         if image_response.status_code != 200:
#             print('Failed to fetch image ' + url)
#             continue

#         image = image_response.content
#         file_name = f'{id}.{extension}'

#         with open(f'{SOURCE_DIR}/{file_name}', 'wb') as f:
#             f.write(image)

#     metadata_file = f'{SOURCE_DIR}/metadata.jsonl'
#     with open(metadata_file, 'w') as f:
#         for index in range(len(images)):
#             line = images[index]
#             f.write(json.dumps(line) + '\n')

def preprocess(input_dir: str):
    if os.path.exists(f'{OUTPUT_DIR}'):
        shutil.rmtree(OUTPUT_DIR)

    with open(f'{input_dir}/metadata.jsonl', 'r') as f:
        images = [json.loads(line) for line in f]

    all_tags = {tag for image in images for tag in image['tags']}
    all_tags = list(sorted(all_tags))

    tags2id = {tag: id for id, tag in enumerate(all_tags)}

    splits = {
        'train': [],
        'validation': [],
    }
    for dir in splits.keys():
        if not os.path.exists(f'{OUTPUT_DIR}/{dir}'):
            os.makedirs(f'{OUTPUT_DIR}/{dir}')

    for index in range(len(images)):
        # id, extension, tags = images[index]['id'], images[index]['metadata']['original']['extension'], images[index]['tags']
        # file_name = f'{id}.{extension}'
        tags = images[index]['tags']
        file_name = images[index]['file_name']

        # For multi label classifications, use one-hot encoding
        encoded_tags = [0] * len(all_tags)
        for tag in tags:
            encoded_tags[tags2id[tag]] = 1.0

        for split in splits.keys():
            splits[split].append({
                'file_name': file_name,
                'tags': encoded_tags
            })
            shutil.copyfile(f'{input_dir}/{file_name}', f'{OUTPUT_DIR}/{split}/{file_name}')

    for split, metadata in splits.items():
        metadata_file = f'{OUTPUT_DIR}/{split}/metadata.jsonl'
        with open(metadata_file, 'w') as f:
            for line in metadata:
                f.write(json.dumps(line) + '\n')

    with open(f'{OUTPUT_DIR}/tags.json', 'w') as f:
        f.write(json.dumps(all_tags))

if __name__ == '__main__':
    # download_images()
    # preprocess(SOURCE_DIR)

    read_digikam_files(SOURCE_DIGIKAM_DIR)
    preprocess(SOURCE_DIGIKAM_DIR)
