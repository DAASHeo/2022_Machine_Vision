import sys
import numpy as np, cv2

image = cv2.imread('profile.jpg', cv2.IMREAD_GRAYSCALE) #영상 읽기

if image is None: #예외처리
    print('Image load failed!')
    sys.exit()

resize = cv2.resize(image, dsize=(240, 360)) #이미지 사이즈 재조정
dst = cv2.normalize(resize, None, 0, 255, cv2.NORM_MINMAX) #normalize
dst2 = cv2.equalizeHist(resize) #equalize

#resize, normalize, equalize한 결과 출력
cv2.imshow("resize", resize)
cv2.imshow("normalize", dst)
cv2.imshow("equalize", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

