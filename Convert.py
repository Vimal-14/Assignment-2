import cv2
import numpy as np

img = cv2.imread("tree.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imwrite("temp/tree/gray.png",imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imwrite("temp/tree/blur.png",imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imwrite("temp/tree/Canny.png",imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imwrite("temp/tree/Dialated.png",imgDialation)
cv2.imshow("Erosion Image", imgEroded)
cv2.imwrite("temp/tree/eroded.png",imgEroded)
cv2.waitKey(0)