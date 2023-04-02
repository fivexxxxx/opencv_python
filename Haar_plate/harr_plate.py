import cv2
import numpy as np
#引入tesseract库
import pytesseract
# 首先在WIN上的安装
# 下载地址： https://digi.bib.uni-mannheim.de/tesseract/
# 配置环境变量：
# 添加环境变量：TESSDATA_PREFIX
# 比如路径：C:\Program Files (x86)\Tesseract-OCR\tessdata
# 中文支持：下载语言包，地址：https://tesseract-ocr.github.io/tessdoc/Data-Files
# 将下载的语言包chi_sim.traineddata，复制到安装路径下TESSDATA_PREFIX 指定的路径下
#下载地址  https://github.com/opencv/opencv/tree/master/data/haarcascades

#1  创建 HAAR级联器  #识别车牌
plate=cv2.CascadeClassifier("./haarcascades/haarcascade_russian_plate_number.xml")

#2 导入车牌识别的图片,并将其灰度化
img=cv2.imread('car.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#3 进行车牌识别
#[[x,y,w,h]]
plates=plate.detectMultiScale(gray,1.1,5)
for (x,y,w,h) in plates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#对车牌预处理
# 提取ROI
roi=gray[y:y+h,x:x+w]
#二值化
ret,roi_bin=cv2.threshold(roi,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#识别车牌
print(pytesseract.image_to_string(roi,lang='chi_sim+eng',config='--psm 8 --oem 3'))

cv2.imshow('roi_bin',roi_bin)
cv2.imshow('img',img)
cv2.waitKey()


















