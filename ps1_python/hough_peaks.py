#!/usr/bin/env python3

import numpy as np


def hough_peaks(H, numpeaks):
    #peaks = np.zeros((1, 2), dtype=np.uint8)
    i = 0

    for r in range(0, H.shape[0]-1):
        for c in range(0, H.shape[1]-1):
            if H[r, c] > 200:
                if i == 0:
                    peaks = [r,c]
                    i = 1
                else:
                    peaks = np.vstack([peaks, [[r,c]]])

    if peaks.shape[0] > numpeaks:
        lines = np.zeros((peaks.shape[0] - numpeaks, 1), dtype=np.uint8)
        k = 0
        for i in range(0, peaks.shape[0]):
            count = 0
            counted = False
            for j in range(0, peaks.shape[0]):
                if H[peaks[i, 0], peaks[i, 1]] < H[peaks[j, 0], peaks[j, 1]]:
                    count += 1
                if (count == numpeaks) & (~counted):
                    lines[k] = i
                    k += 1
                    counted = True

        peaks = np.delete(peaks, lines, 0)

    return peaks
