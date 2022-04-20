import sys
import numpy as np, cv2

src = cv2.imread('rgbColor.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

B, G, R = cv2.split(src)

cv2.imshow("original", src)
cv2.imshow("bluechannel", B)
cv2.imshow("greenchannel", G)
cv2.imshow("redchannel", R)

cv2.waitKey(0)

cv2.destroyAllWindows()

