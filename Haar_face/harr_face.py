import cv2
import numpy as np
#下载地址  https://github.com/opencv/opencv/tree/master/data/haarcascades

#print(cv2.getBuildInformation())

#1  创建 HAAR级联器
#facer=cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
#识别眼睛
facer=cv2.CascadeClassifier("./haarcascades/haarcascade_eye.xml")


#2 导入人脸识别的图片,并将其灰度化

img=cv2.imread('huang.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#3 进行人脸识别
#[[x,y,w,h]]
faces=facer.detectMultiScale(gray,1.1,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('img',img)
cv2.waitKey()


















