import cv2
import numpy as np

def to_list(img):
    rows, cols, mode = img.shape
    seq=[]
    for y in range(rows):
        seq.append([])
        for x in range(cols):
            c = im[y,x]
            tup = (c[2], c[1], c[0])
            seq[y].append(tup)
    return seq

im = cv2.imread("resources/messi.jpg")


def color_bounds(color = 1):
    green = np.uint8([[[0,255,0]]])
    hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    lower, upper = np.array([0,0,0]), np.array([0,0,0])
    for i in range(3):
        if i  == color:
            middle = hsv[0][0][i]
            lower[i] = middle - 10
            upper[i]  = middle + 10
        else:
            lower[i] = 100
            upper[i] = 255
    return lower, upper


def capture_color(color=0):
    cap = cv2.VideoCapture(0)
    lower, upper = color_bounds(color)
    print(lower, upper)
    while(1):

        # Take each frame
        _, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV


        #lower = np.array([110,100,100])
        #upper = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower, upper)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()


