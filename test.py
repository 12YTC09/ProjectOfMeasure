
#0919

import numpy as np 
import cv2
import os


test_pic=cv2.imread('-10.bmp')


cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))


#將圖轉成灰階
img_gray=cv2.cvtColor(test_pic,cv2.COLOR_BGR2GRAY)



#apply binary thresholding
#調整圖形閥值

ret, thresh = cv2.threshold(img_gray, 65, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



# visualize the binary image


cv2.drawContours(thresh, contours, -1, (65,255,0), 3)
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.imwrite('image_thres1.jpg', thresh)
cv2.destroyAllWindows()









