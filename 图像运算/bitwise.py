import cv2
import numpy as np

#创建背景图片--非操作
# img=np.ones((200,200),np.uint8)
# img[50:150,50:150]=255
# cv2.imshow('img',img)
# new_img=cv2.bitwise_not(img)
# cv2.imshow('new_img',new_img)
# key=cv2.waitKey(0)

#创建背景图片--与操作
# img1=np.ones((200,200),np.uint8)
# img2=np.ones((200,200),np.uint8)
# img1[20:120,20:120]=255
# img2[80:180,80:180]=255
# new_img=cv2.bitwise_and(img1,img2)
# cv2.imshow('img',img1)
# cv2.imshow('img2',img2)
# cv2.imshow('new_img',new_img)

#创建背景图片--或操作
img1=np.ones((200,200),np.uint8)
img2=np.ones((200,200),np.uint8)
img1[20:120,20:120]=255
img2[80:180,80:180]=255
new_img=cv2.bitwise_or(img1,img2)
cv2.imshow('img',img1)
cv2.imshow('img2',img2)
cv2.imshow('new_img',new_img)

#创建背景图片--异或操作
img1=np.ones((200,200),np.uint8)
img2=np.ones((200,200),np.uint8)
img1[20:120,20:120]=255
img2[80:180,80:180]=255
new_img=cv2.bitwise_ors(img1,img2)
cv2.imshow('img',img1)
cv2.imshow('img2',img2)
cv2.imshow('new_img',new_img)


key=cv2.waitKey(0)

if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
