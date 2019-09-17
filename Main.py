import sys
import numpy as np
from numpy.linalg import svd

import Maracana1 as points
from sympy import *

import cv2


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
    return u, v


def main():
    x1 = points.x1
    x2 = points.x2
    x3 = points.x3
    x4 = points.x4
    x5 = points.x5
    x6 = points.x6

    y1 = points.y1
    y2 = points.y2
    y3 = points.y3
    y4 = points.y4
    y5 = points.y5
    y6 = points.y6

    z1 = points.z1
    z2 = points.z2
    z3 = points.z3
    z4 = points.z4
    z5 = points.z5
    z6 = points.z6

    u1 = points.u1
    u2 = points.u2
    u3 = points.u3
    u4 = points.u4
    u5 = points.u5
    u6 = points.u6

    v1 = points.v1
    v2 = points.v2
    v3 = points.v3
    v4 = points.v4
    v5 = points.v5
    v6 = points.v6

    A = np.array([
        [x1, y1, z1, 1, 0, 0, 0, 0, -u1 * x1, -u1 * y1, -u1 * z1, -u1],
        [0, 0, 0, 0, x1, y1, z1, 1, -v1 * x1, -v1 * y1, -v1 * z1, -v1],
        [x2, y2, z2, 2, 0, 0, 0, 0, -u2 * x2, -u2 * y2, -u2 * z2, -u2],
        [0, 0, 0, 0, x2, y2, z2, 2, -v2 * x2, -v2 * y2, -v2 * z2, -v2],
        [x3, y3, z3, 3, 0, 0, 0, 0, -u3 * x3, -u3 * y3, -u3 * z3, -u3],
        [0, 0, 0, 0, x3, y3, z3, 3, -v3 * x3, -v3 * y3, -v3 * z3, -v3],
        [x4, y4, z4, 4, 0, 0, 0, 0, -u4 * x4, -u4 * y4, -u4 * z4, -u4],
        [0, 0, 0, 0, x4, y4, z4, 4, -v4 * x4, -v4 * y4, -v4 * z4, -v4],
        [x5, y5, z5, 5, 0, 0, 0, 0, -u5 * x5, -u5 * y5, -u5 * z5, -u5],
        [0, 0, 0, 0, x5, y5, z5, 5, -v5 * x5, -v5 * y5, -v5 * z5, -v5],
        [x6, y6, z6, 6, 0, 0, 0, 0, -u6 * x6, -u6 * y6, -u6 * z6, -u6],
        [0, 0, 0, 0, x6, y6, z6, 6, -v6 * x6, -v6 * y6, -v6 * z6, -v6]
    ])
    U, S, V = svd(A)

    P = V[11].reshape(3, 4)

    m11 = P[0][0]
    m12 = P[0][1]
    m13 = P[0][2]
    m14 = P[0][3]
    m21 = P[1][0]
    m22 = P[1][1]
    m23 = P[1][2]
    m24 = P[1][3]
    m31 = P[2][0]
    m32 = P[2][1]
    m33 = P[2][2]
    m34 = P[2][3]

    x = x1
    y = y1
    z = z1
    u = (m11 * x + m12 * y + m13 * z + m14) / (m31 * x + m32 * y + m33 * z + m34)
    v = (m21 * x + m22 * y + m23 * z + m24) / (m31 * x + m32 * y + m33 * z + m34)
    print(u)


if __name__ == '__main__':
    main()
