# Mini Project 15

import cv2
import os
def grayscale(input, output):
    # Creating an output folder if the provided one does not exist
    if not os.path.exists(output):
        os.makedirs(output)

    # Getting file names of the images in the input folder:
    image_files = os.listdir(input)

    for image_file in image_files:
        input_path = os.path.join(input, image_file)
        output_path = os.path.join(output, image_file)
        # Reading the images
        image = cv2.imread(input_path)
        # Converting the images to B/W
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Saving the black n white images
        cv2.imwrite(output_path, gray_image)

    print("All The coloured images of the input folder have successfully been converted to greyscale!")

input_path = 'D:\Coding\Python programmming\summer_school\images'
output_path = 'B/W_images'
grayscale(input_path, output_path)