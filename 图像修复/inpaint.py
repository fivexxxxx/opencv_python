import cv2
import numpy as np
#展示时效果不理想嘿嘿，，截图问题，就是原始图片和mask图片对不上。
img=cv2.imread('fruits.png')
mask=cv2.imread('mask.png',0)

dst=cv2.inpaint(img,mask,5,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)

cv2.waitKey()



