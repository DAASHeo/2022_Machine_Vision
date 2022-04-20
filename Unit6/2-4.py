import sys
import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread('dark.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print('Image load failed!')
    sys.exit()

resize = cv2.resize(image, dsize=(240, 360))
hist = cv2.calcHist([resize], [0], None, [256], [0, 256])

src = cv2.add(resize, 50)
shist = cv2.calcHist([src], [0], None, [256], [0, 256])

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
dhist = cv2.calcHist([dst], [0], None, [256], [0, 256])

dst2 = cv2.equalizeHist(src)
ehist = cv2.calcHist([dst2], [0], None, [256], [0, 256])

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

