import sys
import numpy as np, cv2
import matplotlib.pyplot as plt

src = cv2.imread('rgbColor.jpg')#영상 읽기

if src is None: #예외처리
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb) #컬러 공간 변환 BGR -> YCrCb
y, cr, cb = cv2.split(src_ycrcb) #채널 분리
hist = cv2.calcHist([y], [0], None, [256], [0, 256])# Y에 대한 히스토그램 계산

y_cont = cv2.add(y, 100) #적당한 명암비로 조절
chist = cv2.calcHist([y_cont], [0], None, [256], [0, 256]) #명암비 조절한 이미지에 대한 히스토그램 계산

y_norm = cv2.normalize(y_cont, None, 0, 255, cv2.NORM_MINMAX) #normalize
nhist = cv2.calcHist([y_norm], [0], None, [256], [0, 256]) #normalize한 이미지에 대한 히스토그램 계산

y_equal = cv2.equalizeHist(y_cont) #equalize
ehist = cv2.calcHist([y_equal], [0], None, [256], [0, 256]) #equalize한 이미지에 대한 히스토그램 계산

#4개의 히스토그램을 함께 출력
plt.subplot(221), plt.plot(hist)
plt.subplot(222), plt.plot(chist)
plt.subplot(223), plt.plot(nhist)
plt.subplot(224), plt.plot(ehist)

cv2.imshow("Y", y)
cv2.imshow("Increase contrast", y_cont)
cv2.imshow("Normalize", y_norm)
cv2.imshow("Equalize", y_equal)
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()

