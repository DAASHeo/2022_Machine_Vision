import numpy as np, cv2

image = cv2.imread("profile.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

resize = cv2.resize(image, dsize=(240, 360)) #사이즈 재조정

dst1 = cv2.Sobel(np.float32(resize), cv2.CV_32F, 1, 0, 3)
dst2 = cv2.Sobel(np.float32(resize), cv2.CV_32F, 0, 1, 3)
dst1 = cv2.convertScaleAbs(dst1)
dst2 = cv2.convertScaleAbs(dst2)

cv2.imshow("original", resize)
cv2.imshow("dst1-vertical_OpenCV", dst1)
cv2.imshow("dst2-vertical_OpenCV", dst2)
cv2.waitKey()

cv2.destroyAllWindows()