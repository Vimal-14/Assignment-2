import cv2
import numpy as np
img = 'dog.png'
img1 = 'Group.jpeg.jpg'
img2 = 'lambo.png'
img3 = 'tree.png'

img_read = cv2.imread(img)
img1_read = cv2.imread(img1)
img2_read = cv2.imread(img2)
img3_read = cv2.imread(img3)

cv2.imshow("Image 1",img_read)
cv2.imshow("Image 2",img1_read)
cv2.imshow("Image 3",img2_read)
cv2.imshow("Image 4",img3_read)

cv2.waitKey(0)