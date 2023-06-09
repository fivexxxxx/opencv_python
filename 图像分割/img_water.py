import cv2
import numpy as np

from matplotlib import pyplot as plt

#步骤
#1 通过2二值法得到黑白图片
#2 通过形态学获得背景

#读图片
img=cv2.imread('coin.png')  #
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #cv2.THRESH_OTSU自动阈值

#开运算
kernel=np.ones((3,3),np.int8)
kai=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
#膨胀
bg=cv2.dilate(kai,kernel,iterations=1)

#获取前景物体
dist=cv2.distanceTransform(kai,cv2.DIST_L2,5)
ret,fg=cv2.threshold(dist,0.7*dist.max(),255,cv2.THRESH_BINARY)

# plt.imshow(dist,cmap='gray')
# plt.show()
# exit()
#获取未知区域
fg=np.uint8(fg)
unknow=cv2.subtract(bg,fg)

#创建联通域
ret,marker=cv2.connectedComponents(fg)#前景
marker=marker+1 #背景
marker[unknow==255]=0   #未知区域
#分水岭法-分割图像
result=cv2.watershed(img,marker)
img[result==-1]=[0,0,255]
cv2.imshow('img',img)


cv2.imshow('thresh',thresh)
cv2.imshow('bg',bg)
cv2.imshow('fg',fg)
cv2.imshow('unknow',unknow)


key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
