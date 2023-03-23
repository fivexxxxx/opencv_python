import cv2
import numpy as np

#读图片
dog=cv2.imread('dog.jpg')
print(dog.shape[0])
new=cv2.flip(dog,0) #   参数：0 上下翻转，1 左右翻转，-1 上下+左右翻转


cv2.imshow('dog',dog)
cv2.imshow('new',new)


key=cv2.waitKey(0)

if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
