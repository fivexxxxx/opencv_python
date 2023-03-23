import cv2
import numpy as np
from utils import *

img=np.zeros((480,640,3),np.uint8)

#画线，坐标点(x,y)    颜色      线宽      类型
cv2.line(img,(10,20),(300,400),(0,0,255),5,4)
cv2.line(img,(100,120),(400,420),(0,0,255),5,16)


cv2.imshow('img',img)
cv2.waitKey(0)


















