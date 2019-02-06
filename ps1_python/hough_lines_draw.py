#!/usr/bin/env python3

import cv2
import numpy as np


def hough_lines_draw(img, img_name, peaks, thetas, rhos):
    for r in range(0, peaks.shape[0]):
        theta = thetas[peaks[r, 1]]
        rho = rhos[peaks[r, 0]]
        a = np.cos(np.deg2rad(theta))
        b = np.sin(np.deg2rad(theta))
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    name = 'ps1_python/output/' + img_name
    cv2.imwrite(name, img)
