import cv2
import numpy as np

#获得单应性矩阵
def get_homo(img1,img2):
    # pass
    # #先转灰度
    # gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    # gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    #创建SIFT特征检测器
    sift=cv2.xfeatures2d.SIFT_create()

    #计算描述子和特征点
    kp1,des1=sift.detectAndCompute(img1,None)
    kp2,des2=sift.detectAndCompute(img2,None)
    #创建特征匹配器
    bf = cv2.BFMatcher(cv2.NORM_L1)
    match = bf.knnMatch(des1, des2,k=2)
    #过滤特征点，找出有效的特征匹配点
    verify_ratio=0.8
    verify_matches=[]
    for m1,m2 in match:
        if m1.distance <0.8*m2.distance:
            verify_matches.append(m1)
    #查找单应性矩阵
    if len(verify_matches)>=4:
        img1_pts=[]
        img2_pts=[]
        for m in verify_matches:
            img1_pts.append(kp1[m.queryIdx].pt)
            img2_pts.append(kp2[m.trainIdx].pt)
        img1_pts=np.float32(img1_pts).reshape(-1,1,2)
        img2_pts = np.float32(img2_pts).reshape(-1, 1, 2)
        H,_=cv2.findHomography(img1_pts,img2_pts,cv2.RANSAC,5.0)
        return H
    else:
        print('err:Not enough matches...')
        exit()

#拼接图片
def stitch_image(img1,img2,H):
    #1 获得每张图片的4个角点
    #2 对图片进行变化（用矩阵对图片进行旋转，平移）
    #3 创建大图，拼接两个小图
    #获得原始图的高、宽
    h1,w1=img1.shape[:2]
    h2, w2 = img2.shape[:2]
    #四个角点
    img1_dims=np.float32([[0,0],[0,h1],[w1,h1],[w1,0]]).reshape(-1,1,2)
    img2_dims = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    #图像变换
    img1_transform = cv2.perspectiveTransform(img1_dims, H)
    # print(img1_dims)
    # print(img2_dims)
    # print(img1_transform)
    #求最大和最小值--为了创大图
    result_dims=np.concatenate((img2_dims,img1_transform),axis=0)
    #print(result_dims)
    [x_min,y_min]=np.int32(result_dims.min(axis=0).ravel()-0.5)
    [x_max, y_max] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
    #平移距离
    transform_dist=[-x_min,-y_min]
    #构建坐标
    transform_array=np.array([[1,0,transform_dist[0]],
                              [0,1,transform_dist[1]],
                              [0,0,1]])

    #透视变化+ transform_array.dot(H)-(实现平移)
    result_img=cv2.warpPerspective(img1,transform_array.dot(H),(x_max-x_min,y_max-y_min))
    #图1，图2拼接
    result_img[transform_dist[1]:transform_dist[1]+h2,transform_dist[0]:transform_dist[0]+w2]=img2

    return result_img



#读图片
img1=cv2.imread('1.png')  #
img2=cv2.imread('2.png')  #

img1=cv2.resize(img1,(480,360))
img2=cv2.resize(img2,(480,360))
inputs=np.hstack((img1,img2))

#单应性矩阵
H=get_homo(img1,img2)

#拼接图像
rst_img=stitch_image(img1,img2,H)

#cv2.imshow('hh',inputs)
cv2.imshow('aa',rst_img)

# #先转灰度
# gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# #查找单应性矩阵
# if len(good)>=4:
#     srcPts=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
#     dstPts=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
#     H,_=cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5.0)
#     #透视变化
#     h,w=img1.shape[:2]
#     pts=np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
#     dst=cv2.perspectiveTransform(pts,H)
#
#     cv2.polylines(img2,[np.int32(dst)],True,(0,0,255))
# else:
#     exit()
#
#
# img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)
#
# cv2.imshow('search',img3)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
