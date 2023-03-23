import cv2
import numpy as np
from utils import *

curShape=0
startpos=(0,0)

#创建背景图片
img=np.zeros((480,640,3),np.uint8)

#鼠标回调函数
def mouse_callback(event,x,y,flags,userdata):
    #print(event,x,y,flags,userdata)
    global curShape,startpos
    if(event & cv2.EVENT_LBUTTONDOWN==cv2.EVENT_LBUTTONDOWN):
        startpos=(x,y)
    elif (event & cv2.EVENT_LBUTTONUP==cv2.EVENT_LBUTTONUP):
        if curShape==0:
            cv2.line(img, startpos, (x, y),(0, 0, 255))
        elif curShape==1:
            cv2.rectangle(img, startpos, (x, y),(0, 0, 255))
        elif curShape==2:
            a2=(x-startpos[0])
            b2=(y-startpos[1])
            r=int((a2**2+b2**2)**0.5)
            cv2.circle(img, startpos, r,(0, 0, 255))
        else:
            print("no")
#创建窗口
cv_create_win('mouse',cv2.WINDOW_NORMAL,640,360)

#设置鼠标回调函数
cv2.setMouseCallback('mouse',mouse_callback,"123")

while True:
    cv2.imshow("mouse",img)
    key = cv2.waitKey(1) & 0xFF #
    if (key == ord('q')):
        break
    elif key==ord('l'):# draw lines
        curShape=0
    elif key == ord('r'):   #draw rectangel
        curShape = 1
    elif key == ord('c'):   #draw circle
        curShape = 2

cv2.destroyAllWindows()
