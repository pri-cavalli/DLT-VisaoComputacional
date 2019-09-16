import sys
import numpy as np

def main():
    A = np.array([
        [x1, y1, z1, 1, 0, 0, 0, 0, -u1*x1, -u1*y1, -u1*z1, -u1],
        [0, 0, 0, 0, x1, y1, z1, 1, -v1*x1, -v1*y1, -v1*z1, -v1],
        [x2, y2, z2, 2, 0, 0, 0, 0, -u2*x2, -u2*y2, -u2*z2, -u2],
        [0, 0, 0, 0, x2, y2, z2, 2, -v2*x2, -v2*y2, -v2*z2, -v2],
        [x3, y3, z3, 3, 0, 0, 0, 0, -u3*x3, -u3*y3, -u3*z3, -u3],
        [0, 0, 0, 0, x3, y3, z3, 3, -v3*x3, -v3*y3, -v3*z3, -v3],
        [x4, y4, z4, 4, 0, 0, 0, 0, -u4*x4, -u4*y4, -u4*z4, -u4],
        [0, 0, 0, 0, x4, y4, z4, 4, -v4*x4, -v4*y4, -v4*z4, -v4],
        [x5, y5, z5, 5, 0, 0, 0, 0, -u5*x5, -u5*y5, -u5*z5, -u5],
        [0, 0, 0, 0, x5, y5, z5, 5, -v5*x5, -v5*y5, -v5*z5, -v5],
        [x6, y6, z6, 6, 0, 0, 0, 0, -u6*x6, -u6*y6, -u6*z6, -u6],
        [0, 0, 0, 0, x6, y6, z6, 6, -v6*x6, -v6*y6, -v6*z6, -v6]
    ])
    M = np.array([[m11], [m12], [m13], [m14], [m21], [m22], [m23], [m24], [m31], [m32], [m33], [m34]])
    result  = np.array([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])

if __name__ == '__main__':
    main()
    
