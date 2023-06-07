import cv2

frameWidth = 640
frameHeight = 480
frameSize = (frameWidth,frameHeight)
cap = cv2.VideoCapture("sample-1.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)
    output = cv2.VideoWriter('temp/video/Video_1.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,frameSize)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        # This adds delay and keyword 'q' to close the window
        break