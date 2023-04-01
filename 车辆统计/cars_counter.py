import cv2
import numpy as np
#报错AttributeError: module 'cv2' has no attribute 'bgsegm'，需要安装
#pip install opencv-contrib-python
#方便去除车辆上小的块，比如车牌，车灯也可能未过滤掉，需要如下两个参数配合过滤
min_w=90
min_h=90
#定义线高
line_high=410
offset=8
#统计车的个数
carno=0
#存放有效车辆数组
cars=[]
#计算车辆的中心点
def center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy

cap=cv2.VideoCapture('cars.mp4')
bgsub=cv2.bgsegm.createBackgroundSubtractorMOG()
#形态学的kernel
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))#还有其他如：MORPH_ELLIPSE;MORPH_CROSS

while True:
    ret,frame=cap.read()
    #print(frame.shape)
    if (ret==True):
        #先灰度，再去噪
        cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #去背景前先去噪
        blur=cv2.GaussianBlur(frame,(3,3),5)
        #去背景
        mask=bgsub.apply(blur)
        #腐蚀，去掉小的脏块
        erode=cv2.erode(mask,kernel)
        #膨胀,还原放大
        dilate=cv2.dilate(erode,kernel,iterations=2)    #参数 iterations =x 可以指定膨胀次数
        #闭运算-去除内部小点
        close=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)   #可以做多次
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)  # 可以做多次
        #查找轮廓
        cnts,h=cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #画一条检测线
        cv2.line(frame,(10,line_high),(300,line_high),(255,255,0),3)
        #遍历轮廓
        for(i,c) in enumerate(cnts):
            (x,y,w,h)=cv2.boundingRect(c)
            #对车辆宽和高判断，验证是否是有效车辆
            isValid=(w>=min_w) and (h>=min_h)
            if(not isValid):
                continue
            #这里是有效的车辆
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cpoint=center(x,y,w,h)
            cars.append(cpoint)

            for (x,y) in  cars:
               if((y>line_high-offset) and (y<line_high+offset)):
                    carno=carno+1
                    cars.remove((x,y))
                    print(carno)

        cv2.putText(frame,"Cars Count:"+str(carno),(40,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)
        cv2.imshow('frame', frame)
        #cv2.imshow('video',mask)
        #cv2.imshow('dilate', close)



    key = cv2.waitKey(50)
    if (key == ord('q')):
        break




cap.release()
cv2.destroyAllWindows()






