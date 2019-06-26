import cv2
import numpy as np

image = cv2.imread("135fQpO.png")

#Detecting edges

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 5) 

edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#Applying Filter to Colour
colour = cv2.bilateralFilter(image, 9, 300, 300)


#Developing the Animated version of the image by combining colour and edges
animation = cv2.bitwise_and(colour, colour, mask=edges)

cv2.imshow("Image", image)

cv2.imshow("Animation", animation)

cv2.waitKey(0)
cv2.destroyAllWindows()