import sys
import numpy as np
import cv2

src = cv2.imread('profile.jpg', cv2.IMREAD_GRAYSCALE)

resize = cv2.resize(src, dsize=(240, 360))

gaussian = cv2.GaussianBlur(resize, (0,0), 3)

cv2.imshow('src', resize)
cv2.imshow('Gaussian',gaussian)
cv2.waitKey()
