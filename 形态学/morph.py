import cv2
import numpy as np
#开运算和闭运算
#读图片
#img=cv2.imread('jjjdot.png')  #开运算
img=cv2.imread('jjjdot2.png')  #开运算


#kernel=np.ones((3,3),np.uint8)#自建核
#系统核
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))#还有其他如：MORPH_ELLIPSE;MORPH_CROSS

#dst=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)    #开运算--先腐蚀后膨胀
dst=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)    #闭运算--先膨胀后腐蚀
cv2.imshow('img',img)
cv2.imshow('dst',dst)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
