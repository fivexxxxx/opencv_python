# opencv_python
opencv相关笔记库的源码分享。








# #车牌识别部分：# #

Tesseract 使用的步骤说明：

首先在WIN上的安装Tesseract

下载地址： https://digi.bib.uni-mannheim.de/tesseract/

配置环境：

添加环境变量：TESSDATA_PREFIX 
 
比如路径：C:\Program Files (x86)\Tesseract-OCR\tessdata

中文支持：

下载语言包，地址：https://tesseract-ocr.github.io/tessdoc/Data-Files

将下载的语言包chi_sim.traineddata，复制到安装路径下TESSDATA_PREFIX 指定的路径下即可。
