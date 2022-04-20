import sys
import numpy as np, cv2

src = cv2.imread('ycrcbColor.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

YCC_img = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

Y, Cr, Cb = cv2.split(YCC_img)

cv2.imshow("original", src)
cv2.imshow("Y", Y)
cv2.imshow("Cr", Cr)
cv2.imshow("Cb", Cb)

cv2.waitKey(0)

cv2.destroyAllWindows()
