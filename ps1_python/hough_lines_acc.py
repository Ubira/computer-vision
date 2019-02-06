#!/usr/bin/env python3

import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import os.path

def hough_lines_acc(img, rho_res=1, thetas=np.arange(0,180,1)):
    height, width = img.shape
    rho_size = int(math.sqrt(pow(height,2) + pow(width,2)))
    rhos = np.arange(0,rho_size*rho_res,1)
    H = np.zeros((len(rhos),len(thetas)),dtype=np.uint8)
    for c in range(0,height-1):
        for r in range(0,width-1):
            if img[r,c] == 255:
                for k in thetas:
                    rhos[k] = c*math.cos(k) - r*math.sin(k)
                    H[rhos[k],thetas[k]] += 1;

    return H, thetas, rhos
