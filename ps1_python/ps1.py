#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
from hough_lines_acc import *
from hough_peaks import *
from hough_lines_draw import *

if __name__ == '__main__':
    img = cv2.imread('ps1_python/input/ps1-input0.png', cv2.IMREAD_GRAYSCALE)
    img_edges = cv2.Canny(img, 0, 1)
    cv2.imwrite('ps1_python/output/ps1-1-a-1.png', img_edges)

    H, thetas, rhos = hough_lines_acc(img_edges)
    cv2.imwrite('ps1_python/output/ps1-2-a-1.png', H)

    peaks = hough_peaks(H, 10)
    P = cv2.imread('ps1_python/output/ps1-2-a-1.png')

    for i in range(0, len(peaks)):
        x, y = peaks[i]
        P = cv2.rectangle(P, (y - 2, x - 2), (y + 2, x + 2), (0, 255, 0))

    cv2.imwrite('ps1_python/output/ps1-2-b-1.png', P)

    img_color = cv2.imread('ps1_python/input/ps1-input0.png', cv2.IMREAD_COLOR)
    hough_lines_draw(img_color, 'ps1-2-c-1.png', peaks, thetas, rhos)
