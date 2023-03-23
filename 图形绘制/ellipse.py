import cv2
import numpy as np
from utils import *

img=np.zeros((480,640,3),np.uint8)
#矩形
cv2.rectangle(img,(10,10),(100,100),(0,0,255),-1)
#圆
cv2.circle(img,(320,240),100,(0,0,255))
cv2.circle(img,(320,240),3,(0,0,255),-1)#-1 表示填充

#椭圆
#           图  ,中心点，  长宽半，角度，起始角，结束角，颜色
#度-》顺时针
cv2.ellipse(img,(320,240), (100,50),0,     0,    360,  (0,0,255))
#多边形




#
cv2.imshow('img',img)
cv2.waitKey(0)


















