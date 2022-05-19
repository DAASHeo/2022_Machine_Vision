import numpy as np, cv2
from filters import filter

image = cv2.imread("filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# 샤프닝 마스크 원소 지정 
data1 = np.array([[0, -1, 0],
        [-1, 5, -1],
         [0, -1, 0]])
mask1 = np.array(data1, np.float32).reshape(3, 3)

sharpen1 = filter(image, mask1)                     # 회선 수행 – 저자 구현 함

sharpen1 = cv2.convertScaleAbs(sharpen1)

cv2.imshow("image", image)
cv2.imshow("sharpen1", sharpen1)  # 윈도우 표시 위한 형변환

cv2.waitKey(0)