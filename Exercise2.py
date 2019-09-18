import numpy as np
from numpy.linalg import svd, inv
from Maracana2 import *
# import cv2
# 297, 23
cornerKickMeters = 27.5


def drawOffsideLineOnMaracana2Image():
    A = generateA()
    P = generateCameraProjectionMatrix(A)
    givenPixel = np.array([0, 0])

    givenRealWorldPoint = calculateRealWorldPoint(givenPixel, P)
    topCornerKickRealWorldPoint = np.array([givenRealWorldPoint[0], - cornerKickMeters])
    bottomCornerKickRealWorldPoint = np.array([givenRealWorldPoint[0], cornerKickMeters])

    topCornerKickPixel = calculatePixels(topCornerKickRealWorldPoint, P)
    bottomCornerKickPixel = calculatePixels(bottomCornerKickRealWorldPoint, P)

    print "\n\n3d"
    print "--expect:"
    print givenRealWorldPoint
    print "be equal to:"
    print [0, 0]
    print "--expect:"
    print calculateRealWorldPoint(np.array([(297 - originX), (23 - originY)]), P)
    print "be equal to:"
    print bottomCornerKickRealWorldPoint
    print "--expect:"
    print calculateRealWorldPoint(np.array([(264 - originX), (343 - originY)]), P)
    print "be equal to:"
    print topCornerKickRealWorldPoint
    print "\n2d"
    print [givenPixel[0] + originX, givenPixel[1] + originY]
    print "--expect:"
    print [topCornerKickPixel[0] + originX, topCornerKickPixel[1] + originY]
    print "be equal to:"
    print [401, 238]
    print "--expect:"
    print [bottomCornerKickPixel[0] + originX, bottomCornerKickPixel[1] + originY]
    print "be equal to:"
    print [352, 23]


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
        [x1, y1, 0, 1, 0, 0, 0, 0, -u1 * x1, -u1 * y1, 0, -u1],
        [0, 0, 0, 0, x1, y1, 0, 1, -v1 * x1, -v1 * y1, 0, -v1],
        [x2, y2, 0, 1, 0, 0, 0, 0, -u2 * x2, -u2 * y2, 0, -u2],
        [0, 0, 0, 0, x2, y2, 0, 1, -v2 * x2, -v2 * y2, 0, -v2],
        [x3, y3, 0, 1, 0, 0, 0, 0, -u3 * x3, -u3 * y3, 0, -u3],
        [0, 0, 0, 0, x3, y3, 0, 1, -v3 * x3, -v3 * y3, 0, -v3],
        [x4, y4, 0, 1, 0, 0, 0, 0, -u4 * x4, -u4 * y4, 0, -u4],
        [0, 0, 0, 0, x4, y4, 0, 1, -v4 * x4, -v4 * y4, 0, -v4]
    ])


def generateCameraProjectionMatrix(A):
    _, _, V = svd(A)    
    P = V[len(V) - 1].reshape(3, 4)
    return np.delete(P, 2, 1)

def calculateRealWorldPoint(point, cameraMatrix):
    u = point[0]
    v = point[1]
    inverseHomography = inv(cameraMatrix)
    worldCoordinates = inverseHomography.dot(np.array([u, v, 1]))

    realWorldX = worldCoordinates[0] / worldCoordinates[2]
    realWorldY = worldCoordinates[1] / worldCoordinates[2]

    return [realWorldX, realWorldY]
    