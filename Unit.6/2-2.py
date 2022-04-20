import sys
import numpy as np, cv2, math

src = cv2.imread('hsvColor.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

HSV_img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(HSV_img)

cv2.imshow("original", src)
cv2.imshow("H", H)
cv2.imshow("S", S)
cv2.imshow("V", V)

cv2.waitKey(0)

cv2.destroyAllWindows()