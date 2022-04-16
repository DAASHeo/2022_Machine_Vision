import sys
import numpy as np, cv2

src = cv2.imread('rgbColor.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

