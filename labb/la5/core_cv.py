import cv2
import numpy as np


def no_blue(img):
    img[:,:,2] = 200

def add_weighted(img1, img2, w1, w2):
    """w1 (0-1)"""
    return cv2.addWeighted(img1, w1, img2, w2, 0)


def paste_opaque(src, target, show_all=False):
    """"""
    rows, cols, channels = src.shape
    tr, tc, tch = target.shape
    roi = target[tr-rows:tr, 0:cols] #bottom left corner
    srcgray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(srcgray,10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    target_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
    src_fg  = cv2.bitwise_and(src, src, mask=mask)
    target_paste = cv2.add(target_bg, src_fg)
    target[tr- rows:tr, 0:cols] = target_paste #bottom left corner
    if show_all:
        show_image(target, "target")
        show_image(target_paste, "target_paste")
        show_image(mask, "mask")
        show_image(mask_inv, "mask_inv")
        show_image(srcgray, "srcgray")
    return target

def show_image(img, title="opencv res"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



messi = cv2.imread('resources/messi.jpg')
logo = cv2.imread('resources/logo.jpg')
merge = paste_opaque(logo, messi, True)
show_image(merge)