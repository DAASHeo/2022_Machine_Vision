import numpy as np, cv2

# 영상 읽기
image1 = cv2.imread("add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생") #예외 처리

alpha, beta = 0.6, 0.7 #곱셈 비율
add_img = cv2.addWeighted(image1, alpha, image2, beta, 0) #두 영상 비율에 따른 더하기

dst = cv2.hconcat([image1, add_img, image2]) #3개의 이미지 한 윈도우에 표시

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()