import cv2
import numpy as np

blocksiez=2
ksize=3
k=0.04

#读图片
img=cv2.imread('harris.png')  #
#先转灰度
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#角点检测
dst=cv2.cornerHarris(gray,blocksiez,ksize,k)
#角点展示
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('harris',img)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
