#!/usr/bin/env python3

import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import os.path

def hough_lines_acc(img, rho_res=1, thetas=np.arange(0,180,1)):
    height, width = img.shape
    rhos = np.arange(-200,199,rho_res)
    H = np.zeros((len(rhos),len(thetas)),dtype=np.uint8)
    for c in range(0,height-1):
        for r in range(0,width-1):
            if img[r,c] == 255:
                for k in range(0,179):
                    thetas[k] = math.atan2(r,c)
                    rhos[k] = c*math.cos(thetas[k]) + r*math.sin(thetas[k])
                    H[rhos[k],thetas[k]] += 1;

    return H, thetas, rhos
