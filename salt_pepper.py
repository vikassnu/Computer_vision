import random
import cv2

def add_salt_pepper_noise(img):
    r,c = img.shape   # dimension of image
    no_of_pixels = random.randint(200,10000)
    # pick some pixels randomly, then colored with white and black
    for i in range(no_of_pixels):
        y_axis=random.randint(0,r-1)
        x_axis=random.randint(0,c-1)
        img[y_axis][x_axis] = 255

    no_of_pixels = random.randint(200,100000)
    for i in range(no_of_pixels):
        y_axis=random.randint(0,r-1)
        x_axis=random.randint(0,c-1)
        img[y_axis][x_axis]=0

    return img

img = cv2.imread('colored.jpg',cv2.IMREAD_GRAYSCALE)  # covert colored image to grey
# salt and pepper noise can be applied to greyscale image only
cv2.imwrite('salt_pepper.jpg',add_salt_pepper_noise(img)) #store the converted image

print("successful")



