import cv2
import numpy as np

#读图片
#img=cv2.imread('dog.jpg')  #均值滤波使用
#img=cv2.imread('gaussian.jpg')  #高斯滤波试验
#img=cv2.imread('mean.jpg')  #中值滤波使用
img=cv2.imread('lena.png')  #双边滤波使用

#方法1--自己创建的卷积核
#kernel=np.ones((5,5),np.float32)/25
#dst=cv2.filter2D(img,-1,kernel)

#方法2--均值滤波函数
#dst=cv2.blur(img,(5,5))#5核的大小

#高斯滤波
#dst=cv2.GaussianBlur(img,(5,5),sigmaX=1)

#中值滤波
#dst=cv2.medianBlur(img,7)

#双边滤波
dst=cv2.bilateralFilter(img,7,20,50)



cv2.imshow('img',img)
cv2.imshow('dst',dst)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
