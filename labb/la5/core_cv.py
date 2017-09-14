import cv2
import numpy as np

img = cv2.imread('resources/messi.jpg')
h, w, mode = img.shape

img[:,:,2] = 200
cv2.imshow('No blue', img)


cv2.waitKey(0)
cv2.destroyAllWindows()