import os
import tensorflow.compat.v1 as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format


WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models/'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'my_ssd_mobnet/'

def create_label_map():
    labels = [
        {'name':'A', 'id':1},
        {'name':'B', 'id':2},
        {'name':'C', 'id':3},
        {'name':'D', 'id':4},
        {'name':'E', 'id':5},
        {'name':'F', 'id':6},
        {'name':'G', 'id':7}
    ]

    with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')

def create_records():
    os.system(f"{SCRIPTS_PATH + '/generate_tfrecord.py'} -x {IMAGE_PATH + '/train'} -l {ANNOTATION_PATH + '/label_map.pbtxt'}"
              f"-o {ANNOTATION_PATH + '/train.record'}")


#-x "C:\Users\calvi\PycharmProjects\IKCOVI\Tensorflow\workspace\images\\train" -l "C:\Users\calvi\PycharmProjects\IKCOVI\Tensorflow\workspace\\annotations\label_map.pbtxt" -o "C:\Users\calvi\PycharmProjects\IKCOVI\Tensorflow\workspace\\annotations\\train.record"
#-x "C:\Users\calvi\PycharmProjects\IKCOVI\Tensorflow\workspace\images\\test" -l "C:\Users\calvi\PycharmProjects\IKCOVI\Tensorflow\workspace\\annotations\label_map.pbtxt" -o "C:\Users\calvi\PycharmProjects\IKCOVI\Tensorflow\workspace\\annotations\\test.record"

config = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
print(config)
