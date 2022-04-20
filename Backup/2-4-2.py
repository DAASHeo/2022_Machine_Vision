import sys
import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist/shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img, 0)

image = cv2.imread('dark.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print('Image load failed!')
    sys.exit()

bins, ranges = [256], [0, 256]
hist = cv2.calcHist([])

resize = cv2.resize(image, dsize=(240, 360))
src = cv2.add(resize, 50)
shist = cv2.calcHist([src], [0], None, [256], [0, 256])
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
dhist = cv2.calcHist([dst], [0], None, [256], [0, 256])

cv2.imshow("increase contrast", src)
cv2.imshow("normalize", dst)

plt.subplot(121), plt.plot(shist)
plt.subplot(122), plt.plot(dhist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

