import cv2
import numpy as np


#读图片
img=cv2.imread('meanshift.png')  #
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
mean_img=cv2.pyrMeanShiftFiltering(img,20,30)

img_canny=cv2.Canny(mean_img,150,300)

contours,_=cv2.findContours(img_canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,0,255),2)


cv2.imshow('img_canny',img_canny)
cv2.imshow('mean_img',mean_img)
cv2.imshow('img',img)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
