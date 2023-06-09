import cv2  #默认读取的格式是 BGR
import  numpy as np
import matplotlib.pyplot as plt
from utils import *

img=cv2.imread('1.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print(img)
ret,thresh1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO_INV)
titles=['1','binary','binary_inv','trunc','toZero','tozero_inv']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
