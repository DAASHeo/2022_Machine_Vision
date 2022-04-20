import sys
import numpy as np, cv2
import matplotlib.pyplot as plt

src = cv2.imread('rgbColor.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(src_ycrcb)
hist = cv2.calcHist([y], [0], None, [256], [0, 256])

y_cont = cv2.add(y, 100)
chist = cv2.calcHist([y_cont], [0], None, [256], [0, 256])

y_norm = cv2.normalize(y_cont, None, 0, 255, cv2.NORM_MINMAX)
nhist = cv2.calcHist([y_norm], [0], None, [256], [0, 256])

y_equal = cv2.equalizeHist(y_cont)
ehist = cv2.calcHist([y_equal], [0], None, [256], [0, 256])

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

