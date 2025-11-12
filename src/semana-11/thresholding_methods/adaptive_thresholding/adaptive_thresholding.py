import os
import numpy as np
import argparse 
import cv2

path = "C:/projects/IC/Projeto 1/Original ROI images/healthy"

for filename in os.listdir(path):
    image_path = os.path.join(path, filename)

    image = cv2.imread(image_path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("Original", image)

    thresh = cv2.adaptiveThreshold(blurred, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
    cv2.imshow("Mean Thresh", thresh)

    thresh = cv2.adaptiveThreshold(blurred, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
    cv2.imshow("Gaussian Thresh", thresh)
    cv2.waitKey(0)

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the input image")
# args = vars(ap.parse_args())


# image = cv2.imread(args["image"])
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(image, (5, 5), 0)
# cv2.imshow("Original", image)

# thresh = cv2.adaptiveThreshold(blurred, 255, 
#     cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
# cv2.imshow("Mean Thresh", thresh)

# thresh = cv2.adaptiveThreshold(blurred, 255, 
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
# cv2.imshow("Gaussian Thresh", thresh)
# cv2.waitKey(0)