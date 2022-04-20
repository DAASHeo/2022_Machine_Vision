import numpy as np, cv2

image = np.zeros((300, 400), np.uint8) #300행 400열의 행렬 생성
image[:] = 100 # 회색(100)바탕 영상 생성

title= 'Window' #title 변수에 'Window'라는 윈도우 이름 할당
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE) #크기 재조정 불가능한 윈도우 생성
cv2.imshow(title, image)
cv2.resizeWindow(title, 500, 600)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()