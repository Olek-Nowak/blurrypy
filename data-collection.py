import cv2
import os
cam = cv2.VideoCapture(0)
num = 1
while os.path.exists('./datasets/'+str(num)):
    num = num + 1
os.mkdir('./datasets/'+str(num))
imCount = 1
success = True
while success:
    success, img = cam.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./datasets/'+str(num)+'/img'+str(imCount)+'.png',img_gray)
    imCount = imCount + 1
    cv2.imshow("Data-grab", img_gray)
    key = cv2.waitKey(300)
# ESC to escape loop
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()