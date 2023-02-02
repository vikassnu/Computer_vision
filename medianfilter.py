import cv2
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from  numpy import divide, int8, multiply, ravel, sort, zeros_like

def median_filter(gray_img, mask=3):
    bd = int(mask/2)
    median_img = zeros_like(gray_img)
    for i in range(bd,gray_img.shape[0]-bd):
        for j in range(bd,gray_img.shape[1]-bd):
            kernel = ravel(gray_img[i-bd: i + bd + 1, j - bd : j + bd + 1])
            median = sort(kernel)[int8(divide((multiply(mask,mask)),+2)+1)]
            median_img[i,j]=median
    return median_img


if __name__ == "__main__":
    # read original image
    img = imread("salt_pepper2.jpg")
    # turn image in gray scale value
    gray = cv2.cvtColor(img,cv2.COLOR_BG2GRAY)

    # get values with two different mask size
    median3x3 = median_filter(gray, 3)
    median5x5 = median_filter(gray, 5)

    # show result images
    imshow("median filter with 3x3 mask", median3x3)
    imshow("median filter with 5x5 mask", median5x5)
    cv2.waitKey(0)