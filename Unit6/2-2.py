import sys
import numpy as np, cv2, math

src = cv2.imread('hsvColor.jpg') #영상 읽기

if src is None: #예외처리
    print('Image load failed!')
    sys.exit()

HSV_img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) #컬러 공간 변환 BGR->HSV
H, S, V = cv2.split(HSV_img) #채널 분리

cv2.imshow("original", src) #원본 이미지 윈도우에 띄우기
cv2.imshow("H", H) #H 채널 윈도우에 띄우기
cv2.imshow("S", S) #S 채널 윈도우에 띄우기
cv2.imshow("V", V) #V 채널 윈도우에 띄우기

cv2.waitKey(0)

cv2.destroyAllWindows()