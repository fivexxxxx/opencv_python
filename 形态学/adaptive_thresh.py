import cv2
import numpy as np

#读图片
img=cv2.imread('math.png')  #

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dst=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,0)
print(dst.shape)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('dst',dst)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
