import cv2
import numpy as np
#视频的前景和背景分离

cap=cv2.VideoCapture('mog.mp4')

#方法1
#mog=cv2.bgsegm.createBackgroundSubtractorMOG()
#方法2--好处可以计算阴影部分，缺点是产生噪点
#mog=cv2.createBackgroundSubtractorMOG2()
#方法3 好处，可算出阴影，同时减少噪点，，，缺点，默认时，开始时间好长时间没有显示，调整参考帧数量
mog=cv2.bgsegm.createBackgroundSubtractorGMG(10)

while(True):
    ret,frame=cap.read()
    fgmask=mog.apply(frame)

    cv2.imshow('img',fgmask)
    k=cv2.waitKey(10)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()