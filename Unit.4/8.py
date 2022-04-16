import numpy as np, cv2

img1 = np.zeros((200, 300), np.uint8) #300행 400열의 행렬 생성
img2 = np.zeros((200, 300), np.uint8)
img1[:] = 0
img2[:] = 0

title1, title2 = 'WINDOW1', 'WINDOW2'

height, width = img1.shape

cv2.imshow(title1, img1)
cv2.imshow(title2, img2)

cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, width, height)

cv2.waitKey(0)
cv2.destroyAllWindows()