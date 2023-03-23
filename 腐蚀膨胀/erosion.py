import cv2
import  numpy as np
from utils import *

img=cv2.imread('dfbb.jpg')

kernel=np.ones((3,3),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)
dilate=cv2.dilate(erosion,kernel,iterations=1)

cv_show('img',img)
cv_show('erosion',erosion)
cv_show('dilate',dilate)



