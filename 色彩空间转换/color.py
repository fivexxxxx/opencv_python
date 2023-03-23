import cv2
import numpy as np
from utils import *

def callback():
    pass

#创建窗口
cv_create_win('color',cv2.WINDOW_NORMAL,640,360)
img=cv2.imread('1.jpg')

colorspaces=[cv2.COLOR_BGR2RGBA,\
             cv2.COLOR_BGR2GRAY,\
             cv2.COLOR_BGR2HSV]
cv2.createTrackbar('curcolor','color',0,len(colorspaces),callback)

while True:
    index=cv2.getTrackbarPos('curcolor','color')
    cvt_img=cv2.cvtColor(img,colorspaces[index])

    cv2.imshow('color',cvt_img)
    key = cv2.waitKey(1)  #
    if (key & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()









