
import numpy as np
import math

class Trackball:
    def __init__(self, theta=0, distance=15):
        self.theta = theta
        self.phi = 0
        self.radius = distance
        self.matrix = self._compute_matrix()

    def _compute_matrix(self):
        t = np.identity(4)
        t[2, 3] = -self.radius

        r1 = np.identity(4)
        r1[:3, :3] = self._rotation_matrix([1, 0, 0], math.radians(self.theta))

        r2 = np.identity(4)
        r2[:3, :3] = self._rotation_matrix([0, 1, 0], math.radians(self.phi))

        return np.dot(np.dot(r1, r2), t)

    def drag_to(self, x, y, dx, dy):
        self.theta += dy
        self.phi += dx
        self.matrix = self._compute_matrix()

    def _rotation_matrix(self, axis, angle):
        axis = np.asarray(axis)
        axis = axis / math.sqrt(np.dot(axis, axis))
        a = math.cos(angle / 2.0)
        b, c, d = -axis * math.sin(angle / 2.0)
        return np.array([
            [a*a + b*b - c*c - d*d, 2*(b*c - a*d),     2*(b*d + a*c)],
            [2*(b*c + a*d),     a*a + c*c - b*b - d*d, 2*(c*d - a*b)],
            [2*(b*d - a*c),     2*(c*d + a*b),     a*a + d*d - b*b - c*c]
        ])
