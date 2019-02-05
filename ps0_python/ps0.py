#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os.path

if __name__ == '__main__':
    # 1
    img = cv2.imread('input/mona-lisa.png',1)
    img2 = cv2.imread('input/bicycle.png',1)
    cv2.imwrite('output/ps0-1-a-1.png',img)
    cv2.imwrite('output/ps0-1-a-2.png',img2)
    # print(img.shape)
    # print(img.dtype)
    # color = [0,0,255]
    # constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value = color)
    # cv2.imshow('Imagem 1',constant)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # 2
    # OpenCV treats images as BGR, so changing the red and blue panes gives us a RGB image
    # Swap red and blue channels
    img_rgb = img.copy()
    print(img_rgb.shape)
    # This code doesn't work. Why?!
        # B = img_rgb[:,:,0]
        # G = img_rgb[:,:,1]
        # R = img_rgb[:,:,2]
        # img_rgb[:,:,0] = B
        # img_rgb[:,:,1] = G
        # img_rgb[:,:,2] = R
    img_rgb = img_rgb[:,:,::-1]
    # Another option, but more costly
        # b,g,r = cv2.split(img_rgb)
        # img_rgb = cv2.merge([r,g,b])
    cv2.imwrite('output/ps0-2-a-1.png',img_rgb)

    # Create monochrome image from green channel
    G = img[:,:,1]
    cv2.imwrite('output/ps0-2-b-1.png',G)

    # Create monochrome image from red channel
    R = img[:,:,2]
    cv2.imwrite('output/ps0-2-c-1.png',R)


    # 3
    sizeG = G.shape
    square = G[(int(sizeG[0]/2) - 50):(int(sizeG[0]/2) + 50),(int(sizeG[1]/2) - 50):(int(sizeG[1]/2) + 50)]
    R[(int(sizeG[0]/2) - 50):(int(sizeG[0]/2) + 50),(int(sizeG[1]/2) - 50):(int(sizeG[1]/2) + 50)] = square
    cv2.imwrite('output/ps0-3-a-1.png',R)


    # 4
    # a
    maxValue = G.max()
    minValue = G.min()
    mean = G.mean()
    std = G.std()
    print('The maximum value of the green image is ' + str(maxValue))
    print('The minimum value of the green image is ' + str(minValue))
    print('The mean value of the green image is ' + str(mean))
    print('The standard deviation value of the green image is ' + str(std))

    # b
    # plt.subplot(121), plt.imshow(G)
    G2 = (G.astype(float) - mean)
    G2 = G2 / std
    G2 = G2 * 10
    G2 = G2 + mean
    cv2.imwrite('output/ps0-4-b-1.png',G2)

    # c
    G3 = G.copy()
    G3 = G3.astype(float)
    G3[:,0:(sizeG[1] - 2)] = G3[:,2:(sizeG[1])]
    cv2.imwrite('output/ps0-4-c-1.png',G3)
    # print(G)
    # print('\n')
    # print(G3)
    # print('\n')

    # d

    diffG = G.astype(float) - G3
    cv2.imwrite('output/ps0-4-d-1.png',diffG)
    #print(diffG)

    # 5
    # a
    # Generating gaussian (normal) noise
    img = cv2.imread('input/mona-lisa.png',1)
    shape = img.shape
    noise = np.random.normal(0,20,(shape[0],shape[1]))
    noise = noise.astype(int)
    noise = abs(noise)
    # Other option (better)
    # noise = np.zeros((shape[0],shape[1]), np.uint8)
    # cv2.randn(noise, 0, 20)
    print(noise.max())
    noisy_img = img.copy()
    noisy_img[:,:,1] = noisy_img[:,:,1] + noise
    cv2.imwrite('output/ps0-5-a-1.png',noisy_img)

    #b
    noisy_blue_img = img.copy()
    noisy_blue_img[:,:,0] = noisy_blue_img[:,:,0] + noise
    cv2.imwrite('output/ps0-5-b-1.png',noisy_blue_img)
