import cv2
import numpy as np

maxCorner=1000
ql=0.01
mindistance=10

#读图片
img=cv2.imread('harris.png')  #
#先转灰度
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#角点检测
corners=cv2.goodFeaturesToTrack(gray,maxCorner,ql,mindistance)
#角点展示
corners=np.intp(corners)
for i in corners:
    x,y=i.ravel()   #转一维
    cv2.circle(img,(x,y),3,(255,0,0),-1)



cv2.imshow('tomasi',img)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
