import cv2
import numpy as np

#读图片
img1=cv2.imread('cv2.png')  #
img2=cv2.imread('cv1.png')  #
#先转灰度
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#创建SIFT特征检测器
sift=cv2.xfeatures2d.SIFT_create()

#计算描述子和特征点
kp1,des1=sift.detectAndCompute(gray1,None)
kp2,des2=sift.detectAndCompute(gray2,None)

#创建匹配器
index_params=dict(algorithm=1,trees=5)
search_params=dict(checks=50)
flann=cv2.FlannBasedMatcher(index_params,search_params)
#对描述子进行匹配计算
match=flann.knnMatch(des1,des2,k=2)
good=[]
for i,(m,n) in enumerate(match):
    if m.distance<0.7*n.distance:
        good.append(m)

#查找单应性矩阵
if len(good)>=4:
    srcPts=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dstPts=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    H,_=cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5.0)
    #透视变化
    h,w=img1.shape[:2]
    pts=np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
    dst=cv2.perspectiveTransform(pts,H)

    cv2.polylines(img2,[np.int32(dst)],True,(0,0,255))
else:
    exit()


img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)

cv2.imshow('search',img3)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
