import cv2

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)    #WINDOW_AUTOSIZE
cv2.resizeWindow('video',640,480)
#获取摄像设备
url="http://192.168.1.4:8080/video" #手机模拟IP摄像头的地址
#cap=cv2.VideoCapture(0)    #参数 0 自动；“xxx.mp4”可以指定视频文件名
cap=cv2.VideoCapture(url)

while True:
    ret,frame=cap.read()
    cv2.imshow('video',frame)

    key=cv2.waitKey(1)  #实时采集视频时这里可以用1，如果视频文件 参数：1000/视频FPS
    if(key & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
