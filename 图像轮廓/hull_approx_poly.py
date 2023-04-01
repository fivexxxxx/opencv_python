import cv2
import numpy as np
def drawShape(src,points):
    i=0
    while i<len(points):
        if(i==len(points)-1):#连线时，如果是最后一个点就连到起始点
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        else:
            x,y=points[i][0]
            x1,y1=points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),3)
        i=i+1

#读图片
img=cv2.imread('finger.png')  #
print(img.shape)
#先转灰度
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
print(gray.shape)
print(binary.shape)
#轮廓查找--
# RETR_EXTERNAL:只找到最大的轮廓；
# RETR_TREE:找出来全部
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
#绘制轮廓   -1是绘制所有，0-x指定绘制某一个轮廓，当前有个三个0，1，2，可分别带人试试。
cv2.drawContours(img,contours,0,(0,0,255),1)
#多边形逼近
e=5 #精度，越小越精细
approx=cv2.approxPolyDP(contours[0],e,True)
drawShape(img,approx)
#凸包
hull=cv2.convexHull(contours[0])
drawShape(img,hull)


cv2.imshow('img',img)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
