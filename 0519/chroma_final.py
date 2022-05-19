import cv2
import sys
import numpy as np

cap1 = cv2.VideoCapture("my.mp4")

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

cap2 = cv2.VideoCapture('personal.mp4')

# 비디오의 속성 값을 받아오기
# 정수 형태로 변환하기 위해 round를 사용
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)) #프레임의 너비
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)) #프레임의 높이
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT)) #동영상 파일의 총 프레임 수
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps = cap1.get(cv2.CAP_PROP_FPS) #초당 프레임 수
delay = int(1000 / fps) # 1프레임과 다음 프레임 사이의 간격 설정

# 출력 동영상 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (w, h))

# 합성 여부를 위한 플래그 선언
composit_flag = False  # 합성 안한 상태

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break

    # composit_flag 플래그가 True일 때에만 합성
    if composit_flag:
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        frame2 = cv2.resize(frame2, (w, h))

        # composit_flag가 True일 경우 HSV공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)  # 녹색 배경 사람 프레임을 HSV 색 공간으로 변환
        mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))  # hsv 색 공간에서 해당 범위 내의 픽셀만을 ROI로 지정
        cv2.copyTo(frame2, mask, frame1)  # frame2에서 mask영상의 roi와 동일한 픽셀 부분만 frame1에 합성

    out.write(frame1)
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # 스페이스바를 누르면 composit_flag 플래그를 변경
    if key == ord(' '):
        composit_flag = not composit_flag
    elif key == 27:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()