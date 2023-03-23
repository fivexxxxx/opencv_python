import cv2
import numpy as np
from utils import *

#创建窗口
cv_create_win('img',cv2.WINDOW_NORMAL,640,480)
img=np.zeros((480,640,3),np.uint8)

roi=img[100:200,100:200]
roi[:,:]=[0,0,255]
roi[10:50,10:50]=[0,255,0]
while True:
    cv2.imshow('img',img)
    #cv2.imshow('img',img)
    key = cv2.waitKey(1)  #
    if (key & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()

