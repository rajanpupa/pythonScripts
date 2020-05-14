import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)
# brightness
cap.set(10, 150)

mycolors = [
    [5, 107, 0, 19, 255, 255],          # orange
    [133, 56, 0, 159, 156, 255],        # purple
    [57, 76, 0, 100, 255, 255]          # green
]

# three mask windows are displayed 
# each will detect specific color specified in mycolors
def findcolor(img, mycolor):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in mycolor:
        lower = np.array( color[0:3] )
        upper = np.array(  color[3:6]  )
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]), mask)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    findcolor(img, mycolors)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

