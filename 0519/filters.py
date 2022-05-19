import numpy as np, cv2

def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                # 회선 결과 저장 행렬
    ycenter, xcenter = rows//2, cols//2

    for i in range(ycenter, rows - ycenter):                # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1           # 관심 영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1           # 관심 영역 너비 범위
            roi = image[y1:y2, x1:x2].astype('float32')     # 관심 영역 형변환
            tmp = cv2.multiply(roi, mask)                   # 회선 적용: 원소 간 곱셈
            dst[i, j] = cv2.sumElems(tmp)(0)                # 출력 화소 저장
    return dst

def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = rows//2, cols//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter, j + v - xcenter
                    sum += image[y, x] * mask[u, v]
            dst[i, j] = sum
    return dst