import numpy as np, cv2, math

image = cv2.imread('cat.jpg')
src = cv2.resize(image, dsize=(400,300))

h, w = src.shape[:2]

a= 47
b= 1.5
rad = a * math.pi / 180  #각도 설정

x = round(h * math.sin(rad)*b + w * math.cos(rad)*b) #창의 크기
y = round(h * math.cos(rad)*b + w * math.sin(rad)*b)
cv2.namedWindow('dst')
# cv2.resizeWindow('dst', width=x, height=y)

aff = np.array([[1, 0, x/2 - w/2], #첫번째 X, 두번째 Y
               [0, 1, y/2 - h/2]], dtype=np.float32)
trans_mat = cv2.warpAffine(src, aff, (x, y),255)

dst_mat = cv2.getRotationMatrix2D((x/2, y/2), a, b)
rot_dst = cv2.warpAffine(trans_mat, dst_mat, (x, y), cv2.INTER_LINEAR)

cv2.imshow('image', src)
cv2.imshow('dst', rot_dst)
cv2.waitKey()