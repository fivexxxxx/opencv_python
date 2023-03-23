import cv2
import numpy as np
from utils import *

img=np.zeros((480,640,3),np.uint8)
#矩形
cv2.rectangle(img,(10,10),(100,100),(0,0,255),-1)

#多边形
pts=np.array([(300,10),(150,100),(450,100)],np.int32)#必须带符号32
cv2.polylines(img,[pts],True,(0,0,255))
#多边形填充不能用 -1
cv2.fillPoly(img,[pts],(255,0,0))

#绘制文本
cv2.putText(img,'hello xiaoniao',(10,200),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))

#
cv2.imshow('img',img)
cv2.waitKey(0)


















