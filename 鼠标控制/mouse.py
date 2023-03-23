import cv2
import numpy as np
from utils import *

def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)

#创建窗口
cv_create_win('mouse',cv2.WINDOW_NORMAL,640,360)

cv2.setMouseCallback('mouse',mouse_callback,"123")

img=np.zeros((480,640,3),np.uint8)

while True:
    cv2.imshow("mouse",img)
    key = cv2.waitKey(1)  #
    if (key & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
