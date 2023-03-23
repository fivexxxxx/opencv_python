import cv2
import numpy as np

#读图片
dog=cv2.imread('dog.jpg')
print(dog.shape)
#创建背景图片,做加法时，两个图片应该尺寸一致。
img=np.ones((dog.shape[0],dog.shape[1],3),np.uint8)*100

result=cv2.add(dog,img)

cv2.imshow('orig',dog)
cv2.imshow('result',result)

orig_1=cv2.subtract(result,img)

cv2.imshow('orig_1',orig_1)

#加法 图片增亮
#除法 图片变暗
#multiply   乘法，图片亮的更快些
#divide     除法，图片暗的更快些


key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
