import numpy as np, cv2

image = cv2.imread("profile.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

resize = cv2.resize(image, dsize=(240, 360)) #사이즈 재조정

# 샤프닝 마스크 원소 지정
sharpening = np.array([[0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0]])

sharpened = cv2.filter2D(resize, -1, sharpening)

cv2.imshow("image", resize)
cv2.imshow("sharpen", sharpened)  # 윈도우 표시 위한 형변환
cv2.waitKey(0)