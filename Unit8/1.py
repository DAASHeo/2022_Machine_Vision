import sys, cv2
import numpy as np

src_original = cv2.imread('cat.jpg',cv2.BGR2GRAY)
if src_original is None:
     print('Image open failed!')
     sys.exit()

src = cv2.resize(src_original,(400,300))

dst = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY)

aff1 = np.array([[1,0,100],[0,1,50]],dtype=np.float32) #좌표를 지정해서 어파인 변환 행렬을 구한다.
dst1 = cv2.warpAffine(src, aff1,(0,0))# CV2.WarpAffine함수로 어파인 변환을 수행한다.

aff2 = np.array([[1, 0.5, 0], [0, 1, 0]],dtype=np.float32)#좌표를 지정해서 어파인 변환 행렬을 구한다.
h,w = src.shape[:2]#width와 height 구함
dst2 = cv2.warpAffine(src, aff2, (w+int(h*0.5), h)) # CV2.WarpAffine함수로 어파인 변환을 수행한다.
# 이때,반환 영상의 크기를 수정한다.

rot = cv2.getRotationMatrix2D((w/2,h/2),45, 1) #사진의 정가운데 좌표를 중심으로 45도 회전하고 스케일이 0.5인 어파인 행렬을 반환
dst3 = cv2.warpAffine(src, rot, (0,0))#어파인 변환을 수행한다.
map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32)
dst5 = cv2.remap(dst3, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)

dst4 = cv2.resize(src,(0,0), fx = 2, fy = 2,  interpolation=cv2.INTER_NEAREST)#스케일 비율을 조절하여 확대된 사진을 얻는다.

cv2.imshow('original',src)
# cv2.imshow('어파인변환함수',dst1)
# cv2.imshow('shear',dst2)
cv2.imshow('rotation',dst)
#cv2.imshow('nocut_resize',dst4)
cv2.waitKey();
cv2.destroyAllWindows()