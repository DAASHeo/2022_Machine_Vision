import sys
import numpy as np, cv2

src = cv2.imread('ycrcbColor.jpg') #영상 읽기

if src is None: #예외처리
    print('Image load failed!')
    sys.exit()

YCC_img = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb) #컬러 공간 변환 BGR -> YCrCb

Y, Cr, Cb = cv2.split(YCC_img) #채널 분리

cv2.imshow("original", src) #원본 이미지 윈도우에 띄우기
cv2.imshow("Y", Y) #Y 채널 윈도우에 띄우기
cv2.imshow("Cr", Cr) #Cr 채널 윈도우에 띄우기
cv2.imshow("Cb", Cb) #Cb 채널 윈도우에 띄우기

cv2.waitKey(0)

cv2.destroyAllWindows()
