import cv2
import numpy as np

#读图片
dog=cv2.imread('dog.jpg')
#创建背景图片,做加法时，两个图片应该尺寸一致。
img=np.ones((dog.shape[0],dog.shape[1],3),np.uint8)*100

result=cv2.addWeighted(dog,0.5, img,0.3,0)

cv2.imshow('orig',dog)
cv2.imshow('result',result)



key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
