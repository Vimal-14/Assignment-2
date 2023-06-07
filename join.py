import cv2
import numpy as np


img = cv2.imread("dog.png")
img1 = cv2.imread("lambo.png")
img2 = cv2.imread("tree.png")

imghor = np.hstack((img,img,img2))
imgver = np.vstack((img,img2))

cv2.imshow("Horizontal",imghor)
cv2.imwrite("temp/join/horizontal.png",imghor)
cv2.imshow("Vertical",imgver)
cv2.imwrite("temp/join/vertical.png",imgver)

cv2.waitKey(0)