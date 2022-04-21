import sys
import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread('dark.jpg', cv2.IMREAD_GRAYSCALE) #영상 읽기

if image is None: #예외처리
    print('Image load failed!')
    sys.exit()

resize = cv2.resize(image, dsize=(240, 360)) #이미지 사이즈 재조정
hist = cv2.calcHist([resize], [0], None, [256], [0, 256]) #재조정한 이미지에 대한 히스토그램 계산

src = cv2.add(resize, 50) #적당한 명암비로 조절
shist = cv2.calcHist([src], [0], None, [256], [0, 256]) #명암비 조절한 이미지에 대한 히스토그램 계산

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX) #normalize
dhist = cv2.calcHist([dst], [0], None, [256], [0, 256]) #normalize한 이미지에 대한 히스토그램 계산

dst2 = cv2.equalizeHist(src) #equalize
ehist = cv2.calcHist([dst2], [0], None, [256], [0, 256]) #equalize한 이미지에 대한 히스토그램 계산

#4개의 히스토그램을 함께 출력
plt.subplot(221), plt.plot(hist)
plt.subplot(222), plt.plot(shist)
plt.subplot(223), plt.plot(dhist)
plt.subplot(224), plt.plot(ehist)

cv2.imshow("resize", resize)
cv2.imshow("increase contrast", src)
cv2.imshow("normalize", dst)
cv2.imshow("equalize", dst2)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

