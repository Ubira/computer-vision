#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os.path
from hough_lines_acc import *

if __name__ == '__main__':
    img = cv2.imread('ps1_python/input/ps1-input0.png',cv2.IMREAD_GRAYSCALE)
    img_edges = cv2.Canny(img,0,1)
    print(img.shape)
    cv2.imwrite('ps1_python/output/ps1-1-a-1.png',img_edges)

    H, rhos, thetas = hough_lines_acc(img_edges)
    print(len(thetas))
    cv2.imwrite('ps1_python/output/ps1-2-a-1.png',H)
    plt.imshow(H)
    plt.show()
