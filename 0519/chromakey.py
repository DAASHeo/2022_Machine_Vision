import numpy as np, sys, cv2

cap1 = cv2.VideoCapture("my.mp4") #내 크로마키 동영상
# 비디오 객체가 정상적으로 open 되었는지 확인
if not cap1.isOpened():
    print('vidieo open failed!')
    sys.exit()

cap2 = cv2.VideoCapture('dsCampus2.mp4') #덕성 캠퍼스
# 비디오 객체가 정상적으로 open 되었는지 확인
if not cap2.isOpened():
    print('vidieo open failed!')
    sys.exit()

#cap1 동영상 width, height 구함
w1 = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('**foreground','-'*15)
print('width x height : {} x {}'.format(w1,h1))
print('**background','-'*15)

#cap2 동영상 width, height 구함
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

#합성 여부 확인을 위한 Flag 설정
compositFlag = False

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break

    # compositFlag가 True일 경우
    if compositFlag:
        ret2, frame2 = cap2.read()
        if not ret2:
            break

        # compositFlag가 True일 경우 HSV공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) # 녹색 배경 사람 프레임을 HSV 색 공간으로 변환
        mask = cv2.inRange(hsv,(50,150,0),(80,255,255)) # hsv 색 공간에서 해당 범위 내의 픽셀만을 ROI로 지정
        cv2.copyTo(frame2, mask, frame1) # frame2에서 mask영상의 roi와 동일한 픽셀 부분만 frame1에 합성

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '): #스페이스 누르면 실행
        compositFlag = not compositFlag
    elif key == 27:
        break

cap1.release()
cap2.release()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('chromakey.mp4', fourcc, fps, (w1, h2))
out.release()

cv2.destroyAllWindows()