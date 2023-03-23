import cv2
def cv_show(name,img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cv_create_win(name,model,width,heigh):
    cv2.namedWindow(name, model)  # WINDOW_AUTOSIZE
    cv2.resizeWindow(name, width, heigh)