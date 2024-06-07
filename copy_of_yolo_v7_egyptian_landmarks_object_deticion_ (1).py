# -*- coding: utf-8 -*-
"""Copy of Yolo v7 Egyptian landmarks object deticion .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BEimmBSexf34ZLTLJCmCd7rpX-etM_Zw
"""

!nvidia-smi

# Commented out IPython magic to ensure Python compatibility.
# Download YOLOv7 repository and install requirements
!git clone https://github.com/WongKinYiu/yolov7
# %cd yolov7
!pip install -r requirements.txt

import os
os.environ["DATASET_DIRECTORY"]="/content/datasets"

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="77ERbH79KHksVbZDufDa")
project = rf.workspace("fatma-saeed-th9nx").project("egypt-landmarks")
version = project.version(2)
dataset = version.download("yolov7")

# Commented out IPython magic to ensure Python compatibility.
# download COCO starting checkpoint
# %cd /content/yolov7
!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt

# Commented out IPython magic to ensure Python compatibility.
# run this cell to begin training
# %cd /content/yolov7
!python train.py --batch 16 --epochs 30 --data {dataset.location}/data.yaml --weights 'yolov7_training.pt' --device 0

# Run evaluation
!python detect.py --weights runs/train/exp/weights/best.pt --conf 0.1 --source {dataset.location}/test/images

#display inference on ALL test images

import glob
from IPython.display import Image, display

i = 0
limit = 10000 # max images to print
for imageName in glob.glob('/content/yolov7/runs/detect/exp/*.jpg'): #assuming JPG
    if i < limit:
      display(Image(filename=imageName))
      print("\n")
    i = i + 1