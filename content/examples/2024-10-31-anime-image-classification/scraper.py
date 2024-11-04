# https://oxylabs.io/blog/python-web-scraping
import requests
import json
import os
import datasets
import shutil
import torch
from PIL import Image
import multiprocessing as mp
import typing
import signal

IMAGE_COUNT=2

from libxmp.utils import file_to_dict

def read_digikam_files(source_dir: str):
    xmp_files = [file for file in os.listdir(source_dir) if file.endswith('.xmp')]
    # For debugging with a small number of images
    # xmp_files= xmp_files[:10]

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

def download_images():
    response = requests.get(
        f'https://api.nekosia.cat/api/v1/images/catgirl?rating=safe&count={IMAGE_COUNT}'
    )
    if response.status_code != 200:
        print('Failed to fetch data ' + str(response.json()))
        return

    data = response.json()

    if not os.path.exists(f'{SOURCE_DIR}'):
        os.makedirs(f'{SOURCE_DIR}')

    images = data['images']
    for index in range(len(images)):
        id, url, extension = images[index]['id'], images[index]['image']['original']['url'], images[index]['metadata']['original']['extension']
        image_response = requests.get(url)
        if image_response.status_code != 200:
            print('Failed to fetch image ' + url)
            continue

        image = image_response.content
        file_name = f'{id}.{extension}'

        with open(f'{SOURCE_DIR}/{file_name}', 'wb') as f:
            f.write(image)

    metadata_file = f'{SOURCE_DIR}/metadata.jsonl'
    with open(metadata_file, 'w') as f:
        for index in range(len(images)):
            line = images[index]
            f.write(json.dumps(line) + '\n')

splits = [
    'train',
    'validation'
]
def write_image(index: int, images: list[dict], all_tags: list[str], tags2id: dict[str, int], input_dir: str, output_dir: str):
    # id, extension, tags = images[index]['id'], images[index]['metadata']['original']['extension'], images[index]['tags']
    # file_name = f'{id}.{extension}'
    tags = images[index]['tags']
    file_name = images[index]['file_name']

    for split in splits:
        shutil.copyfile(f'{input_dir}/{file_name}', f'{output_dir}/{split}/{file_name}')

    # For multi label classifications, use one-hot encoding
    encoded_tags = [0] * len(all_tags)
    for tag in tags:
        encoded_tags[tags2id[tag]] = 1.0
    return{
        'file_name': file_name,
        'tags': encoded_tags
    }

class MetadataWriter:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.files = {}

    # Handle open and exit: https://stackoverflow.com/a/3774396/24068435
    def __enter__(self) -> typing.Self:
        for split in splits:
            self.files[split] = open(f'{output_dir}/{split}/metadata.jsonl', 'w')
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        for f in self.files.values():
            f.close()

    def callback(self, line: str):
        for f in self.files.values():
            f.write(json.dumps(line) + "\n")

def preprocess(input_dir: str, output_dir: str):
    if os.path.exists(f'{output_dir}'):
        shutil.rmtree(output_dir)

    with open(f'{input_dir}/metadata.jsonl', 'r') as f:
        images = [json.loads(line) for line in f]

    all_tags = {tag for image in images for tag in image['tags']}
    all_tags = list(sorted(all_tags))

    tags2id = {tag: id for id, tag in enumerate(all_tags)}

    for dir in splits:
        if not os.path.exists(f'{output_dir}/{dir}'):
            os.makedirs(f'{output_dir}/{dir}')

    # https://www.machinelearningplus.com/python/parallel-processing-python/
    # Handle an KeyboardInterrupt on the parent process: https://stackoverflow.com/questions/72967793/keyboardinterrupt-with-python-multiprocessing-pool
    with mp.Pool(mp.cpu_count(), initializer=signal.signal, initargs=(signal.SIGINT, signal.SIG_IGN)) as pool, MetadataWriter(output_dir) as writer:
        # metadata = pool.starmap_async(write_image, [(index, images, all_tags, tags2id, input_dir, output_dir) for index in range(len(images))]).get()
        for index in range(len(images)):
            pool.apply_async(write_image, args=(index, images, all_tags, tags2id, input_dir, output_dir), callback=writer.callback)

        with open(f'{output_dir}/tags.json', 'w') as f:
            f.write(json.dumps(all_tags))

        pool.close()
        pool.join()


import sys

if __name__ == '__main__':
    # download_images()
    # preprocess(SOURCE_DIR)

    if len(sys.argv) < 3:
        print('Usage: scraper.py <source_dir> <output_dir>')
        sys.exit(1)
    source_dir = sys.argv[1]
    output_dir = sys.argv[2]
    read_digikam_files(source_dir)
    preprocess(source_dir, output_dir)
