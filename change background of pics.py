import cv2
import numpy as np
 
def cvtBackground(path,color):

    im=cv2.imread(path)
    im_hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)#BGR和HSV的转换
    mask=cv2.inRange(im_hsv,np.array([im_hsv[0,0,0]-5,100,100]),np.array([im_hsv[0,0,0]+5,255,255]))#利用cv2.inRange函数设阈值，去除背景部分
    mask1=mask #在lower_red～upper_red之间的值变成255
    img_median = cv2.medianBlur(mask, 5)#中值滤波，去除一些边缘噪点
    mask = img_median
    mask_inv=cv2.bitwise_not(mask)
    img1=cv2.bitwise_and(im,im,mask=mask_inv)#将人物抠出
    bg=im.copy()
    rows,cols,channels=im.shape
    bg[:rows,:cols,:]=color
    img2=cv2.bitwise_and(bg,bg,mask=mask)#将背景底板抠出
    img=cv2.add(img1,img2)
    image={'im':im,'im_hsv':im_hsv,'mask':mask1,'img':img,'img_median':img_median}
    cv2.startWindowThread()
    for key in image:
        cv2.namedWindow(key)
        cv2.imshow(key,image[key])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
#test
if __name__=='__main__':
    img=cvtBackground('C:\\Users\\sddbook\\Desktop\\mmexport1567593271515.jpg',[255,255,255])
    cv2.imwrite('C:\\Users\\sddbook\\Desktop\\pics of mine\\medianBlur.jpg',img)


