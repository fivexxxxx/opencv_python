import cv2

fourcc=cv2.VideoWriter_fourcc(*'DIVX') # xxx.avi格式视频
vw=cv2.VideoWriter('./out.avi',fourcc,24,(960,540)) #摄像头分辨率多少就写多少
#fourcc=cv2.VideoWriter_fourcc(*'MJPG')
#vw=cv2.VideoWriter('./out2.mp4',fourcc,25,(960,540)) #摄像头分辨率多少就写多少
#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)    #WINDOW_AUTOSIZE
cv2.resizeWindow('video',640,360)
#获取摄像设备
url="http://192.168.1.4:8080/video" #手机模拟IP摄像头的地址
cap=cv2.VideoCapture(url) #参数 0 自动；“xxx.mp4”可以指定视频文件名

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        cv2.imshow('video',frame)
        cv2.resizeWindow('video', 640, 360)
        #保存视频文件
        vw.write(frame)

        key=cv2.waitKey(1)  #实时采集视频时这里可以用1，如果视频文件 参数：1000/视频FPS
        if(key & 0xFF == ord('q')):
            break
    else:
        break
cap.release()
vw.release()
cv2.destroyAllWindows()
