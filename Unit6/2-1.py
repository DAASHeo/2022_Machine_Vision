import sys
import numpy as np, cv2

src = cv2.imread('rgbColor.jpg') #영상 읽기

if src is None: #예외처리
    print('Image load failed!')
    sys.exit()

B, G, R = cv2.split(src) #채널 분리 : 컬러 영상 -> 3채널 분리

cv2.imshow("original", src) #원본 이미지 윈도우에 띄우기
cv2.imshow("bluechannel", B) #Blue 채널 윈도우에 띄우기
cv2.imshow("greenchannel", G) #Green 채널 윈도우에 띄우기
cv2.imshow("redchannel", R) #Red 채널 윈도우에 띄우기

cv2.waitKey(0)

cv2.destroyAllWindows()

