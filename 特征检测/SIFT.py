import cv2
import numpy as np

maxCorner=1000
ql=0.01
mindistance=10

#读图片
img=cv2.imread('harris.png')  #
#先转灰度
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift=cv2.xfeatures2d.SIFT_create()
#kp=sift.detect(gray,None)
kp,des=sift.detectAndCompute(gray,None)
#打印计算子
print(des)
cv2.drawKeypoints(gray,kp,img)

cv2.imshow('sift',img)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
