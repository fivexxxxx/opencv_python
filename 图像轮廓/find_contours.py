import cv2
import numpy as np

#读图片
img=cv2.imread('contours1.png')  #
print(img.shape)
#先转灰度
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
print(gray.shape)
print(binary.shape)
#轮廓查找--
# RETR_EXTERNAL:只找到最大的轮廓；
# RETR_TREE:找出来全部
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

cv2.imshow('img',img)
cv2.imshow('binary',binary)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
