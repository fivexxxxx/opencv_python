import cv2
import numpy as np

#读图片
dog=cv2.imread('dog.jpg')
print(dog.shape)

#创建LOGO
logo=np.zeros((200,200,3),np.uint8)
mask=np.zeros((200,200),np.uint8)
#//绘制logo
logo[20:120,20:120]=[0,0,255]
logo[80:180,80:180]=[0,255,0]
mask[20:120,20:120]=[255]
mask[80:180,80:180]=[255]
#mask求反
m=cv2.bitwise_not(mask)
#选择图片DOG的添加logo位置
roi=dog[0:200,0:200]

tmp=cv2.bitwise_and(roi,roi,mask = m)

dst=cv2.add(tmp,logo)

dog[0:200,0:200]=dst

cv2.imshow('dog',dog)
# cv2.imshow('dst',dst)
# cv2.imshow('tmp',tmp)
# cv2.imshow('m',m)
# cv2.imshow('logo',logo)
# cv2.imshow('mask',mask)


key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
