import numpy as np, cv2

# 600행, 400열의 윈도우를 만들고
img = np.zeros((600, 400, 3), np.uint8) #행렬 생성
img.fill(255) #ndarray 클래스 내부 함수 fill()로 행렬의 원소값을 255로 채운다.
# np.zeros np.ones, np.full 차이점 정확하게 이해할 것!
title = 'rect' #title 변수에 'rect'라는 윈도우 이름 할당

# 영상의 (100, 100) 좌표에 200x300 크기의 빨간색 사각형을 그리시오
p1, p2 = (100, 100), (300, 400)
#(100,100) 좌표부터 시작해야하므로 p1(100,100),사각형의 가로는 200 세로는 300이므로 p1의 x,y좌표에 200,300을 더한 좌표값을 p2에 할당
red = (0, 0, 255) # blue(255,0,0) green(0,255,0) red(0, 0, 255) red라는 변수에 빨간색을 나타내는 색상 선언
cv2.rectangle(img, p1, p2, red) #시작좌표 p1에서 종료좌표인 p2까지 빨간색 사각형을 그린다.

cv2.imshow(title, img) #콜백 함수에서 cv2.imshow()함수를 통해서 행렬을 title창에 영상으로 표시한다.

cv2.waitKey(0) #윈도우에서 키 입력을 기다린다.
cv2.destroyAllWindows() #키가 입력된 후에는 열린 윈도우를 모두 닫는다.