import numpy as np, cv2

def onChange(value):
    None

def onMouse(event, x, y, flags, param):
    global title

    thick = cv2.getTrackbarPos('thick', title)
    radius = cv2.getTrackbarPos('radius', title)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x,y), (x+30, y+30), 0, thick)
        cv2.imshow(title, image)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), radius, 0, thick)
        cv2.imshow(title, image)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

title = "WINDOW1"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar("thick",title, 1, 10, onChange)
cv2.createTrackbar("radius",title, 1, 50, onChange)
cv2.waitKey(0)