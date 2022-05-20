import sys
import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread('cloud.jpg', cv2.IMREAD_GRAYSCALE) #영상 읽기

if image is None: #예외처리
    print('Image load failed!')
    sys.exit()

resize = cv2.resize(image, dsize=(240, 360)) #이미지 사이즈 재조정
hist = cv2.calcHist([resize], [0], None, [256], [0, 256])
dst = cv2.normalize(resize, None, 0, 255, cv2.NORM_MINMAX) #normalize
nhist = cv2.calcHist([dst], [0], None, [256], [0, 256])
dst2 = cv2.equalizeHist(resize) #equalize
eist = cv2.calcHist([hist], [0], None, [256], [0, 256])

plt.subplot(131), plt.plot(hist)
plt.subplot(132), plt.plot(nhist)
plt.subplot(133), plt.plot(eist)

#resize, normalize, equalize한 결과 출력
cv2.imshow("resize", resize)
cv2.imshow("normalize", dst)
cv2.imshow("equalize", dst2)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

