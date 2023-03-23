import cv2
import numpy as np
from utils import *

img=cv2.imread('1.jpg')
#shape的属性包括 高度，宽度 ，通道数
print(img.shape)
#结果 (480, 360, 3)

#图像占用多大空间
print(img.size)
#518400=480*360*3

#每个元素的位深
print(img.dtype)
#uint8

















