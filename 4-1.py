import numpy as np,cv2

image = np.zeros((200,400),np.uint8)
image[:] = 100

title1, title2 = "window1","window2"
cv2.namedWindow(title1, cv2.WINDOW_NORMAL)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 0, 0)

cv2.imshow(title1, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
