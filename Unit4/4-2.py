import numpy as np, cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 255

title1, title2 = "resizefirst", "resizelater"
h, w = image.shape
cv2.namedWindow(title1)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, w, 0)
cv2.resizeWindow(title1, 500, 600)
cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title2, 500, 600)
cv2.waitKey(0)
cv2.destroyAllWindows()