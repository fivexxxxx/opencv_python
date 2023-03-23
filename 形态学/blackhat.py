import cv2
import numpy as np

#读图片
img=cv2.imread('jjjdot2.png')  #

#kernel=np.ones((3,3),np.uint8)#自建核
#系统核
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))#还有其他如：MORPH_ELLIPSE;MORPH_CROSS
dst=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)    #BLACKHAT运算=原图-闭运算

cv2.imshow('img',img)
cv2.imshow('dst',dst)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
