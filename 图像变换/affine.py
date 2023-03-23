import cv2
import numpy as np

#读图片
dog=cv2.imread('dog.jpg')
print(dog.shape[0])
h,w,ch=dog.shape
#方法1
#M=np.float32([[1,0,100],[0,1,0]])   #平移矩阵，自己算
#方法2
#函数求矩阵,旋转角度是逆时针；中心点（x,y)
#M=cv2.getRotationMatrix2D((w/2,h/2),15,1.0)

#方法3
src=np.float32([[200,100],[300,100],[200,500]])
dst=np.float32([[10,200],[200,200],[50,600]])
M=cv2.getAffineTransform(src,dst)

#如果想修改新图片的尺寸，要修改dsize的大小比如：（int(w/2),int(h/2)）
new=cv2.warpAffine(dog,M,(w,h)) #   参数


cv2.imshow('dog',dog)
cv2.imshow('new',new)


key=cv2.waitKey(0)

if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
