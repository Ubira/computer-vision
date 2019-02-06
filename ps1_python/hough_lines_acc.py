#!/usr/bin/env python3

import numpy as np
import math


def hough_lines_acc(img, rho_res=1, thetas=np.arange(0, 180, 1)):
    height, width = img.shape
    rho_size = int(2*(math.sqrt(pow(height, 2) + pow(width, 2))) - 1)
    rhos = np.arange(math.ceil(-rho_size/2), math.ceil(rho_size/2) - 1, rho_res)
    rhos = rhos.astype(int)
    H = np.zeros((len(rhos), len(thetas)), dtype=np.uint8)
    for r in range(0, height-1):
        for c in range(0, width-1):
            if img[r, c] == 255:
                for k in thetas:
                    rho = int(c*np.cos(np.deg2rad(k)) + r*np.sin(np.deg2rad(k)))
                    H[np.where(rhos == rho)[0], k] += 1

    Hmax, Hmin = H.max(), H.min()
    H = (H - Hmin) / (Hmax - Hmin) * 255
    H = H.astype(int)

    return H, thetas, rhos
