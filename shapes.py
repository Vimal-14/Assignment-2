import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.rectangle(img,(0,0),(200,100),(0,255,0),2)

cv2.circle(img,(400,50),25,(255,0,0),4)

cv2.imwrite("temp/shapes/Shapes.png",img)

cv2.imshow("Image",img)

cv2.waitKey(0)