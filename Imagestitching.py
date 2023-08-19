# Import the necessary libraries
import cv2
import numpy as np

# Define the list of images
images = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg",
    "image5.jpg",
    "image6.jpg",
    "image7.jpg",
    "image8.jpg",
    "image9.jpg",
    "image10.jpg"
]

# An empty list to store the images
img_list = []

#To load images in list
for img in images:
    img_list.append(cv2.imread(img))

# Create a stitcher object
stitcher = cv2.Stitcher.create()       #ransac algorithm, image warping are used here
 # as these functions are stored in opencv library

# Stitch the images together
status, stitched_img = stitcher.stitch(img_list)

# Check if the stitching was successful 
if status == cv2.Stitcher_OK:
    print('Your stitched image is ready, please have a look')
    cv2.imwrite("stitched_image.jpg", stitched_img)  #this will save the stitched image 


else:
    print("Error stitching images together.")
