# https://oxylabs.io/blog/python-web-scraping
import requests
import json
import os
import datasets
import shutil

IMAGE_COUNT=2
OUTPUT_DIR = './datasets'

def download_images():
    response = requests.get(
        f'https://api.nekosia.cat/api/v1/images/catgirl?rating=safe&count={IMAGE_COUNT}'
    )
    if response.status_code != 200:
        print('Failed to fetch data ' + str(response.json()))
        exit(0)

    data = response.json()

    for dir in ['train']:
        if not os.path.exists(f'{OUTPUT_DIR}/{dir}'):
            os.makedirs(f'{OUTPUT_DIR}/{dir}')

    all_metadata = []
    images = data['images']
    for index in range(len(images)):
        id, url, extension, tags = images[index]['id'], images[index]['image']['original']['url'], images[index]['metadata']['original']['extension'], images[index]['tags']
        metadata = {
            'id': id,
        }

        image_response = requests.get(url)
        if image_response.status_code != 200:
            print('Failed to fetch image ' + url)
            continue
        image = image_response.content
        with open(f'{OUTPUT_DIR}/train/{id}.{extension}', 'wb') as f:
            f.write(image)
            metadata['file_name'] = f'{id}.{extension}'
        metadata['labels'] = tags
        all_metadata.append(metadata)

    metadata_file = f'{OUTPUT_DIR}/train/metadata.jsonl'
    with open(metadata_file, 'w') as f:
        for metadata in all_metadata:
            f.write(json.dumps(metadata) + '\n')


if __name__ == '__main__':
    shutil.rmtree(OUTPUT_DIR)
    download_images()

    # https://huggingface.co/docs/datasets/image_dataset#imagefolder
    ds = datasets.load_dataset("imagefolder", data_dir="./datasets")

    ds = ds.with_format("torch")
    print(ds)
    print(ds['train'][0])
    print(ds['train'].features)
