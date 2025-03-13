import json
import os
import shutil
from tqdm import tqdm

input_dir = "/mnt/petrelfs/wensiwei/fakevlm/playground/data/train.json"
image_base_dir = "/mnt/petrelfs/wensiwei/fakevlm/playground/data/train"
output_dir = "/mnt/petrelfs/wensiwei/fakevlm/playground/data/train_new.json"



with open(input_dir, "r") as file:
    datas = json.load(file)

os.makedirs(image_base_dir, exist_ok=True)
for data in tqdm(datas):
    # "image": "/mnt/hwfile/opendatalab/bigdata_rs/datasets/FakeVLM/caption-data/GenImage/fake/VQDM_1000_200_08_872_vqdm_00109.png"
    if 'GenImage' in data['image']:
        data['image'] = data['image'].replace('/mnt/hwfile/opendatalab/bigdata_rs/datasets/FakeVLM', '/mnt/hwfile/opendatalab/deepfake/FakeVLM')
        data['dataset_type'] = 'genimage'
        image_relative = os.path.join('genimage', data['image'].split('GenImage/')[-1])
        os.makedirs(image_base_dir + '/genimage/fake', exist_ok=True)
        os.makedirs(image_base_dir + '/genimage/real', exist_ok=True)
        shutil.copy(data['image'], os.path.join(image_base_dir, image_relative))
        data['image'] = image_relative
    # "image": "/mnt/hwfile/opendatalab/bigdata_rs/datasets/Deepfake/FaceForensics++/original_sequences/youtube/c23/frames/395/057.png"
    elif 'FaceForensics++' in data['image']:
        data['image'] = data['image'].replace('opendatalab/', 'opendatalab/deepfake/')
        data['dataset_type'] = 'ff++'
        if 'youtube' in data['image']:
            image_relative = os.path.join('ff++', 'real', data['image'].split('/')[-1])
        else:
            image_relative = os.path.join('ff++', 'fake', data['image'].split('/')[-1])
        os.makedirs(image_base_dir + '/ff++/real', exist_ok=True)
        os.makedirs(image_base_dir + '/ff++/fake', exist_ok=True)
        shutil.copy(data['image'], os.path.join(image_base_dir, image_relative))
        data['image'] = image_relative
    # "image": "/mnt/hwfile/opendatalab/bigdata_rs/datasets/FakeVLM/caption-data/chameleon/fake/9a81652e-b4a7-4ddf-a82c-d78c2f29658c.jpg"
    elif 'chameleon' in data['image']:
        data['image'] = data['image'].replace('/mnt/hwfile/opendatalab/bigdata_rs/datasets/FakeVLM', '/mnt/hwfile/opendatalab/deepfake/FakeVLM')
        data['dataset_type'] = 'chameleon'
        image_relative = os.path.join('chameleon', 'fake', data['image'].split('/')[-1])  
        os.makedirs(image_base_dir + '/chameleon/real', exist_ok=True)
        os.makedirs(image_base_dir + '/chameleon/fake', exist_ok=True)
        shutil.copy(data['image'], os.path.join(image_base_dir, image_relative))
        data['image'] = image_relative
    # "image": ""/mnt/hwfile/opendatalab/bigdata_rs/datasets/FakeVLM/caption-data/satellite/fake/0042260_fake_B.png""
    elif 'satellite' in data['image']:
        data['image'] = data['image'].replace('/mnt/hwfile/opendatalab/bigdata_rs/datasets/FakeVLM', '/mnt/hwfile/opendatalab/deepfake/FakeVLM')
        data['dataset_type'] = 'satellite'
        if data['label'] == 1:
            image_relative = os.path.join('satellite', 'real', data['image'].split('/')[-1])
        else:
            image_relative = os.path.join('satellite', 'fake', data['image'].split('/')[-1])
        os.makedirs(image_base_dir + '/satellite/real', exist_ok=True)
        os.makedirs(image_base_dir + '/satellite/fake', exist_ok=True)
        shutil.copy(data['image'], os.path.join(image_base_dir, image_relative))
        data['image'] = image_relative
    elif 'doc' == data['cate']:
        data['image'] = data['image'].replace('opendatalab/', 'opendatalab/deepfake/')
        data['dataset_type'] = 'doc'
        if data['label'] == 1:
            image_relative = os.path.join('doc', 'real', data['image'].split('/')[-1])
        else:
            image_relative = os.path.join('doc', 'fake', data['image'].split('/')[-1])
        os.makedirs(image_base_dir + '/doc/real', exist_ok=True)
        os.makedirs(image_base_dir + '/doc/fake', exist_ok=True)
        shutil.copy(data['image'], os.path.join(image_base_dir, image_relative))
        data['image'] = image_relative
    else:
        print(data)
        raise('error')
with open(output_dir, "w") as file:
    json.dump(datas, file, indent=4)