import cv2

faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
img = cv2.imread('Group.jpeg.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.00465,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", img)
cv2.imwrite("temp/facedetection/Detected.jpg",img)
cv2.waitKey(0)