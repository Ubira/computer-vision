#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os.path

def hough_lines_acc(img, rho_res=1, thetas=np.arange(-90,90,1)):
    height, width, depth = img.shape
    
