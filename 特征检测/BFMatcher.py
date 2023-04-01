import cv2
import numpy as np

#读图片
img1=cv2.imread('cv2.png')  #
img2=cv2.imread('cv1.png')  #
#先转灰度
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

sift=cv2.xfeatures2d.SIFT_create()

kp1,des1=sift.detectAndCompute(gray1,None)
kp2,des2=sift.detectAndCompute(gray2,None)

bf=cv2.BFMatcher(cv2.NORM_L1)
match=bf.match(des1,des2)
img3=cv2.drawMatches(img1,kp1,img2,kp2,match,None)


cv2.imshow('BF',img3)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
