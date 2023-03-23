import cv2

cv2.namedWindow('img',cv2.WINDOW_NORMAL)    #WINDOW_AUTOSIZE
#读图片
img=cv2.imread('1.jpg')

cv2.resizeWindow('img',640,480)
cv2.imshow('img',img)

#保存图片.png格式
cv2.imwrite('2.png',img)

key=cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
