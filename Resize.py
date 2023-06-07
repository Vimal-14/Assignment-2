import cv2
import numpy as np

img = cv2.imread("dog.png")

imgResize = cv2.resize(img,(150,200))
cv2.imwrite("temp/resize/dog_resize.png",imgResize)

imgScreen = cv2.resize(img,(1600,800))
cv2.imwrite("temp/resize/Screensize_dog.png",imgScreen)

imgCropped = img[0:200,200:500]
cv2.imwrite("temp/crop/dog_cropped.png",imgCropped)

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Screen size image",imgScreen)
cv2.imshow("Cropped image",imgCropped)

cv2.waitKey(0)