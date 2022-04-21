import sys
import numpy as np, cv2

def calc_histo(image, channels, bsize, ranges ):
    shape = bsize if len(channels) >1 else (bsize[0], 1)
    hist = np.zeros((channels, 1), np.float32)
    gap = np.divide(ranges[1::2], bins)

    for row in image:
        for val in row:
            idx = np.divide(val[channels], gap).astype('unit')
            hist[tuple(idx)]+= 1

    return hist