import cv2
import numpy as np

#读图片
img=cv2.imread('harris.png')  #
#先转灰度
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

surf=cv2.ORB_create()
kp,des=surf.detectAndCompute(gray,None)

cv2.drawKeypoints(gray,kp,img)
cv2.imshow('ORB',img)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
