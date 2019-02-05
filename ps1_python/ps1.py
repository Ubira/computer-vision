#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os.path

if __name__ == '__main__':
    img = cv2.imread('input/ps1-input0.png',cv2.IMREAD_GRAYSCALE)
    img_edges = cv2.Canny(img,0,1)
    cv2.imwrite('output/ps1-1-a-1.png',img_edges)
