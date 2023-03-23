import cv2
import numpy as np

#读图片
img=cv2.imread('dog.jpg')  #

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,dst=cv2.threshold(gray,180,255,cv2.THRESH_BINARY)
print(dst.shape)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('dst',dst)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
