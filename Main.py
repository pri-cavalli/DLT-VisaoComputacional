from Exercise1 import drawPlayerOnMaracana1Image
import numpy as np
from numpy.linalg import svd, inv
from Maracana1 import *
import cv2

IMAGE_NAME = 'maracana1.jpg'
IMAGE_WINDOW = 'image'
NO_ACTION = 255
clickPoint = []
hasClicked = False

def main():
    global hasClicked, playerWidth
    img = createImageWindow()
    cv2.imshow(IMAGE_WINDOW, img)
    key = NO_ACTION
    while True:
        while not hasClicked and NO_ACTION == key:
            key = cv2.waitKey(1) & NO_ACTION
        if hasClicked:
            # Exercise 1
            img = drawPlayerOnMaracana1Image(clickPoint, img)
            hasClicked = False
            
        if key == ord('q') or key == ord('Q'):
            cv2.destroyAllWindows()
            quit(0)
        elif key == ord('r') or key == ord('R'):
            img = cv2.imread(IMAGE_NAME)
        cv2.imshow(IMAGE_WINDOW, img)
        key = NO_ACTION
    # drawPlayerOnMaracana1Image()
    # Exercise 2
    # drawOffsideLineOnMaracana2Image()


def createImageWindow():
    img = cv2.imread(IMAGE_NAME)
    cv2.namedWindow(IMAGE_WINDOW)
    cv2.setMouseCallback(IMAGE_WINDOW, getClickPixels)
    return img


def getClickPixels(event, x, y):
    global clickPoint, hasClicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clickPoint = [x, y]
        hasClicked = True

if __name__ == '__main__':
    main()
