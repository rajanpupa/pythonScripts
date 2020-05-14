import cv2

cam = cv2.VideoCapture(0)

# opencv provides many haar cascade classifiers which can be used to detect objects
faceCascade = cv2.CascadeClassifier("open_cv/Resources/_frontalface_default.xml")

img = cv2.imread("webcam_2.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x,y,width,height) in faces:
    cv2.rectangle(img, (x,y), (x+width, y+height), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
