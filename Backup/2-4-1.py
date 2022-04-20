import sys
import numpy as np, cv2
import matplotlib.pyplot as plt

src = cv2.imread('dark.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.resize(src, dsize=(240, 360))

noimage = np.zeros(dst.shape[:2], dst.dtype)
cont = cv2.scaleAdd(dst, 3.0, noimage)

hist = cv2.calcHist([cont], [0], None, [256], [0, 256])

plt.subplot(121), plt.axis('off'), plt.imshow(cont, cmap='gray')
plt.subplot(122), plt.plot(hist)
cv2.imshow("resize", dst)
cv2.imshow("increase contrast", cont)
plt.show()
#
# cv2.imshow("resize", dst)
# cv2.imshow("increase contrast", cont)

cv2.waitKey(0)
cv2.destroyAllWindows()

