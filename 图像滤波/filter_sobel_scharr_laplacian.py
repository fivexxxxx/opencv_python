import cv2
import numpy as np
#读图片
img=cv2.imread('sobel.png')  #

#sobel---y 方向边缘
#d1=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#sobel---x 方向边缘
#d2=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

#沙尔方式--y方向边缘
#d1=cv2.Scharr(img,cv2.CV_64F,1,0)
#沙尔方式--x方向边缘
#d2=cv2.Scharr(img,cv2.CV_64F,0,1)

#拉普拉斯算子方式
lapdst=cv2.Laplacian(img,cv2.CV_64F,ksize=5)


#dst=d1+d2
#dst=cv2.add(d1,d2)#两种都可以

cv2.imshow('img',img)
#cv2.imshow('d1',d1)
#cv2.imshow('d2',d2)
#cv2.imshow('dst',dst)
cv2.imshow('lapdst',lapdst)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
