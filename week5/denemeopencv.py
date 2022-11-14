import cv2
import matplotlib.pyplot as plt
import numpy as np

img =cv2.imread("img.jpg")


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blured = cv2.blur(gray,(5,5))

(thresh, blackAndWhiteImage) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

cv2.imshow("gray",gray)
cv2.imshow("bandw",blackAndWhiteImage)
cv2.imshow("blur",blured)


cv2.waitKey()
cv2.destroyAllWindows()