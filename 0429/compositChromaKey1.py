import numpy as np, sys, cv2

cap1 = cv2.VideoCapture(0)

if not cap1.isOpened():
    print('vidieo open failed!')
    sys.exit()

cap2 = cv2.VideoCapture('dsCampus2.mp4')

if not cap2.isOpened():
    print('vidieo open failed!')
    sys.exit()

w1 = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('**foreground','-'*15)
print('width x height : {} x {}'.format(w1,h1))
print('**background','-'*15)

w2 = round(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
h2 = round(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('width x height : {} x {}'.format(w2,h2))
print('-'*30)

frame_cap1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cap2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_cap1:', frame_cap1)
print('frame_cap2:', frame_cap2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

compositFlag = False

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break

    if compositFlag:
        ret2, frame2 = cap2.read()
        if not ret2:
            break

        frame2 = cv2.resize(frame2,(w1,h1))
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(50,150,0),(150,255,255))
        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '):
        compositFlag = not compositFlag
    elif key == 27:
        break

cap1.release()
cap2.release();

cv2.destroyAllWindows()