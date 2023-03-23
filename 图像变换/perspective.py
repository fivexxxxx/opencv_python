import cv2
import numpy as np

#读图片
book=cv2.imread('book.jpg')
#左上，右上，左下，右下

src=np.float32([[5,70],[259,70],[0,415],[290,415]])
dst=np.float32([[0,0],[290,0],[0,415],[290,415]])

M = cv2.getPerspectiveTransform(src,dst)

new=cv2.warpPerspective(book,M,(290,415))


cv2.imshow('dog',book)
cv2.imshow('new',new)


key=cv2.waitKey(0)

if(key & 0xFF == ord('q')):
    exit()
cv2.destroyAllWindows()
