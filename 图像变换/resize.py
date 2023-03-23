import cv2
import numpy as np

#读图片
dog=cv2.imread('dog.jpg')
print(dog.shape[0])
#new=cv2.resize(dog,(300,300))   #图像变形-非比例缩放

#new=cv2.resize(dog,(int(dog.shape[1]/2),int(dog.shape[0]/2)))   #按比例缩放，图像不变形
#new=cv2.resize(dog,None,fx=0.5,fy=0.5)   #按比例缩放，图像不变形
new=cv2.resize(dog,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)   #按比例缩放，图像不变形,像素损失最少

cv2.imshow('dog',dog)
cv2.imshow('new',new)


key=cv2.waitKey(0)

if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
