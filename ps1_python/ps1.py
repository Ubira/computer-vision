#!/usr/bin/env python3

import cv2
from hough_lines_acc import *
from hough_peaks import *

if __name__ == '__main__':
    img = cv2.imread('ps1_python/input/ps1-input0.png', cv2.IMREAD_GRAYSCALE)
    img_edges = cv2.Canny(img, 0, 1)
    cv2.imwrite('ps1_python/output/ps1-1-a-1.png', img_edges)

    H, rhos, thetas = hough_lines_acc(img_edges)
    cv2.imwrite('ps1_python/output/ps1-2-a-1.png', H)

    peaks = hough_peaks(H, 10)
    P = cv2.imread('ps1_python/output/ps1-2-a-1.png')

    for i in range(0, len(peaks)):
        x, y = peaks[i]
        P = cv2.rectangle(P, (y - 2, x - 2), (y + 2, x + 2), (0, 255, 0))

    cv2.imwrite('ps1_python/output/ps1-2-b-1.png', P)
