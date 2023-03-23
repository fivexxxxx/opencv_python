import cv2
import numpy as np

#读图片
dog=cv2.imread('dog.jpg')
print(dog.shape[0])
new=cv2.rotate(dog,cv2.ROTATE_90_CLOCKWISE) #   参数：cv2.ROTATE_180


cv2.imshow('dog',dog)
cv2.imshow('new',new)


key=cv2.waitKey(0)

if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
