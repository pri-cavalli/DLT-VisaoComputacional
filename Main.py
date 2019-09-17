import numpy as np
from numpy.linalg import svd, inv
from Maracana1 import *


def calculatePixels(x, y, z, cameraMatrix):
    m11 = cameraMatrix[0][0]
    m12 = cameraMatrix[0][1]
    m13 = cameraMatrix[0][2]
    m14 = cameraMatrix[0][3]
    m21 = cameraMatrix[1][0]
    m22 = cameraMatrix[1][1]
    m23 = cameraMatrix[1][2]
    m24 = cameraMatrix[1][3]
    m31 = cameraMatrix[2][0]
    m32 = cameraMatrix[2][1]
    m33 = cameraMatrix[2][2]
    m34 = cameraMatrix[2][3]
    u = (m11 * x + m12 * y + m13 * z + m14) / (m31 * x + m32 * y + m33 * z + m34)
    v = (m21 * x + m22 * y + m23 * z + m24) / (m31 * x + m32 * y + m33 * z + m34)
    return u + 124, v + 157


def calculateRealWorldPoint(point, cameraMatrix):
    u = point[0]
    v = point[1]
    m11 = cameraMatrix[0][0]
    m12 = cameraMatrix[0][1]
    m14 = cameraMatrix[0][3]
    m21 = cameraMatrix[1][0]
    m22 = cameraMatrix[1][1]
    m24 = cameraMatrix[1][3]
    m31 = cameraMatrix[2][0]
    m32 = cameraMatrix[2][1]
    m34 = cameraMatrix[2][3]
    inverseHomography = inv(np.array([np.array([m11, m12, m14]), np.array([m21, m22, m24]), np.array([m31, m32, m34])]))
    worldCordinates = inverseHomography.dot(np.array([u, v, 1]))

    realWorldX = worldCordinates[0] / worldCordinates[2]
    realWorldY = worldCordinates[1] / worldCordinates[2]

    return [realWorldX, realWorldY, 0]


def main():
    A = np.array([
        [x1, y1, z1, 1, 0, 0, 0, 0, -u1 * x1, -u1 * y1, -u1 * z1, -u1],
        [0, 0, 0, 0, x1, y1, z1, 1, -v1 * x1, -v1 * y1, -v1 * z1, -v1],
        [x2, y2, z2, 1, 0, 0, 0, 0, -u2 * x2, -u2 * y2, -u2 * z2, -u2],
        [0, 0, 0, 0, x2, y2, z2, 1, -v2 * x2, -v2 * y2, -v2 * z2, -v2],
        [x3, y3, z3, 1, 0, 0, 0, 0, -u3 * x3, -u3 * y3, -u3 * z3, -u3],
        [0, 0, 0, 0, x3, y3, z3, 1, -v3 * x3, -v3 * y3, -v3 * z3, -v3],
        [x4, y4, z4, 1, 0, 0, 0, 0, -u4 * x4, -u4 * y4, -u4 * z4, -u4],
        [0, 0, 0, 0, x4, y4, z4, 1, -v4 * x4, -v4 * y4, -v4 * z4, -v4],
        [x5, y5, z5, 1, 0, 0, 0, 0, -u5 * x5, -u5 * y5, -u5 * z5, -u5],
        [0, 0, 0, 0, x5, y5, z5, 1, -v5 * x5, -v5 * y5, -v5 * z5, -v5],
        [x6, y6, z6, 1, 0, 0, 0, 0, -u6 * x6, -u6 * y6, -u6 * z6, -u6],
        [0, 0, 0, 0, x6, y6, z6, 1, -v6 * x6, -v6 * y6, -v6 * z6, -v6]
    ])
    U, S, V = svd(A)

    P = V[len(V) - 1].reshape(3, 4)

    givenPoint = np.array([159, 110])
    givenPoint = givenPoint - np.array([origenX, origenY])
    footRealWorldCords = calculateRealWorldPoint(givenPoint, P)
    headRealWorldCords = [footRealWorldCords[0], footRealWorldCords[1], 1.8]

if __name__ == '__main__':
    main()
