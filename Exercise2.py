import numpy as np
from numpy.linalg import svd, inv
from Maracana2 import *
import cv2

cornerKickMetersTop = 24
cornerKickMetersBottom = -42


def drawOffsideLineOnMaracana2Image():
    A = generateA()
    P = generateCameraProjectionMatrix(A)
    givenPixel = np.array([0, 0])
    givenRealWorldPoint = calculateRealWorldPoint(givenPixel, P)

    topCornerKickRealWorldPoint = np.array([givenRealWorldPoint[0], cornerKickMetersTop])
    bottomCornerKickRealWorldPoint = np.array([givenRealWorldPoint[0], cornerKickMetersBottom])

    topCornerKickPixel = calculatePixels(topCornerKickRealWorldPoint, P)
    bottomCornerKickPixel = calculatePixels(bottomCornerKickRealWorldPoint, P)

    img = drawLineOnImage(topCornerKickPixel, bottomCornerKickPixel)
    cv2.imshow('img', img)
    cv2.waitKey(5000)


def calculatePixels(coord, cameraMatrix):
    x = coord[0]
    y = coord[1]
    m11 = cameraMatrix[0][0]
    m12 = cameraMatrix[0][1]
    m13 = cameraMatrix[0][2]
    m21 = cameraMatrix[1][0]
    m22 = cameraMatrix[1][1]
    m23 = cameraMatrix[1][2]
    m31 = cameraMatrix[2][0]
    m32 = cameraMatrix[2][1]
    m33 = cameraMatrix[2][2]
    u = (m11 * x + m12 * y + m13) / (m31 * x + m32 * y + m33)
    v = (m21 * x + m22 * y + m23) / (m31 * x + m32 * y + m33)
    return int(round(u)), int(round(v))

def generateA():
    return np.array([
        [x1, y1, 1, 0, 0, 0, -u1 * x1, -u1 * y1, -u1],
        [0, 0, 0, x1, y1, 1, -v1 * x1, -v1 * y1, -v1],
        [x2, y2, 1, 0, 0, 0, -u2 * x2, -u2 * y2, -u2],
        [0, 0, 0, x2, y2, 1, -v2 * x2, -v2 * y2, -v2],
        [x3, y3, 1, 0, 0, 0, -u3 * x3, -u3 * y3, -u3],
        [0, 0, 0, x3, y3, 1, -v3 * x3, -v3 * y3, -v3],
        [x4, y4, 1, 0, 0, 0, -u4 * x4, -u4 * y4, -u4],
        [0, 0, 0, x4, y4, 1, -v4 * x4, -v4 * y4, -v4],
    ])


def generateCameraProjectionMatrix(A):
    _, _, V = svd(A)    
    return  V[len(V) - 1].reshape(3, 3)

def calculateRealWorldPoint(point, cameraMatrix):
    u = point[0]
    v = point[1]
    inverseHomography = inv(cameraMatrix)
    worldCoordinates = inverseHomography.dot(np.array([u, v, 1]))

    realWorldX = worldCoordinates[0] / worldCoordinates[2]
    realWorldY = worldCoordinates[1] / worldCoordinates[2]

    return [realWorldX, realWorldY]
    
def drawLineOnImage(pixel1, pixel2):
    img = cv2.imread("maracana2.jpg")
    p1 = tuple(pixel1 + np.array([originX, originY]))
    p2 = tuple(pixel2 + np.array([originX, originY]))
    img = cv2.line(img, p1, p2, (255, 0, 0 ), 2)
    return img 