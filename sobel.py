import signal

import cv2
import numpy as np


def sobel_filter(img):

    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]],np.float32)
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]],np.float32)
    Ix = np.zeros(img.shape)
    Iy = np.zeros(img.shape)
    Ix = cv2.filter2D(img,cv2.CV_32F,sobel_x)
    Iy = cv2.filter2D(img, cv2.CV_32F, sobel_y)
    gradient = np.sqrt(np.power(Ix,2) + np.power(Iy,2))
    return gradient

img = cv2.imread("vikas.jpeg",0)
filtered_img = sobel_filter(img)
cv2.imwrite("vikas_filtered_image.jpeg",filtered_img)
print("successful")