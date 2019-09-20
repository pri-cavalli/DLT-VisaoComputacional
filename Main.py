from Exercise1 import drawPlayerOnMaracana1Image
from Exercise2 import drawOffsideLineOnMaracana2Image
import numpy as np
from numpy.linalg import svd, inv
from Maracana1 import *
import cv2

IMAGE_WINDOW = 'image'
NO_ACTION = 255
clickPoint = []
hasClicked = False

def main():
    runExercise(1)
    runExercise(2)
    quit(0)

def runExercise(number):
    print(number)
    if number == 1:
        imgName = 'maracana1.jpg'
    else:
        imgName = 'maracana2.jpg'
    global hasClicked, playerWidth
    img = createImageWindow(imgName)
    cv2.imshow(IMAGE_WINDOW, img)
    key = NO_ACTION
    open = True
    while open:
        while not hasClicked and NO_ACTION == key:
            key = cv2.waitKey(1) & NO_ACTION
        if hasClicked:
            if number == 1:
                img = drawPlayerOnMaracana1Image(clickPoint, img)
            else:
                img = drawOffsideLineOnMaracana2Image(clickPoint, img)
            hasClicked = False

        if key == ord('q') or key == ord('Q'):
            cv2.destroyAllWindows()
            open = False
        elif key == ord('r') or key == ord('R'):
            img = cv2.imread(imgName)
        cv2.imshow(IMAGE_WINDOW, img)
        key = NO_ACTION

def createImageWindow(imageName):
    img = cv2.imread(imageName)
    cv2.namedWindow(IMAGE_WINDOW)
    cv2.setMouseCallback(IMAGE_WINDOW, getClickPixels)
    return img


def getClickPixels(event, x, y, a, v):
    global clickPoint, hasClicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clickPoint = [x, y]
        hasClicked = True

if __name__ == '__main__':
    main()
