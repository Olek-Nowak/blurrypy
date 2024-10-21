import numpy as np
import cv2
import os
# gets run location for later
dirname, filename = os.path.split(os.path.abspath(__file__))
# filter size
filter = (30, 30)
# pre-trained haar cascade classifier
classifier = dirname + "/cascade/haarcascade_frontalface_default.xml"
# self-trained
#classifier = dirname + "/cascade/cascade.xml"
haar_cascade = cv2.CascadeClassifier(classifier)
# open camera - 0 is built-in tag
camera = cv2.VideoCapture(0)
success = True
while success:
    # use webcam
    success, img = camera.read()
    # use single file
    #img = cv2.imread(dirname + '/res/face1.png')
    composite = img
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(img_gray, 1.3, 4)
    for (x, y, width, height) in face:
        # face cutout for processing purposes
        #cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cutout = img[y:y + height, x:x + width]
        cutout = cv2.blur(cutout, filter, cv2.BORDER_DEFAULT)
        composite[y:y + cutout.shape[0], x:x + cutout.shape[1]] = cutout
    cv2.imshow("Wykrywanie twarzy", composite)
    key = cv2.waitKey()
    # key other than spacebar to exit
    if key != 32:
        break
camera.release()
cv2.destroyAllWindows()