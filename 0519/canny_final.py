import cv2
import sys
import numpy as np

cap1 = cv2.VideoCapture("my.mp4")

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

# 비디오의 속성 값을 받아오기
# 정수 형태로 변환하기 위해 round를 사용
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)) #프레임의 너비
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)) #프레임의 높이
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT)) #동영상 파일의 총 프레임 수


fps = cap1.get(cv2.CAP_PROP_FPS) #초당 프레임 수
delay = int(1000 / fps) # 1프레임과 다음 프레임 사이의 간격 설정

# 출력 동영상 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('canny_final.mp4', fourcc, fps, (w, h), isColor=False)

if out.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

while True:
    check, frame = cap1.read()
    # 카메라에서 이미지 얻기. 비디오의 한 프레임씩 읽기,
    # 제대로 프레임을 읽으면 check값이 True 실패하면 False,
    # frame에는 읽은 프레임이 나옴
    if check:

        frame = cv2.GaussianBlur(frame, (5, 5), 0) # 노이즈 제거 - 얻어온 프레임에 대해 5x5 가우시안 필터 먼저 적용
        frame = cv2.Canny(frame, 50, 50)

        out.write(frame)
        cv2.imshow('canny_frame', frame)
        c = cv2.waitKey(1)
        if c & 0xFF == ord(' '):
            break

    else:
        break

cap1.release()
out.release()
cv2.destroyAllWindows()