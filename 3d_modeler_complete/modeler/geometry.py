
import numpy as np

def translation(displacement):
    t = np.identity(4)
    t[0, 3] = displacement[0]
    t[1, 3] = displacement[1]
    t[2, 3] = displacement[2]
    return t

def scaling(scale):
    s = np.identity(4)
    s[0, 0] = scale[0]
    s[1, 1] = scale[1]
    s[2, 2] = scale[2]
    return s

def norm(v):
    return np.linalg.norm(v)

def normalize(v):
    n = norm(v)
    return v / n if n > 0 else v

class AABB:
    def __init__(self, min_v, max_v):
        self.min_v = np.array(min_v)
        self.max_v = np.array(max_v)

    def scale(self, s):
        center = (self.min_v + self.max_v) * 0.5
        half_size = (self.max_v - self.min_v) * 0.5 * s
        self.min_v = center - half_size
        self.max_v = center + half_size

    def ray_hit(self, origin, direction, mat):
        inv = np.linalg.inv(mat)
        o = inv.dot(np.append(origin, 1.0))[:3]
        d = inv.dot(np.append(direction, 0.0))[:3]

        tmin, tmax = -np.inf, np.inf
        for i in range(3):
            if abs(d[i]) < 1e-6:
                if o[i] < self.min_v[i] or o[i] > self.max_v[i]:
                    return (False, None)
            else:
                t1 = (self.min_v[i] - o[i]) / d[i]
                t2 = (self.max_v[i] - o[i]) / d[i]
                t1, t2 = min(t1, t2), max(t1, t2)
                tmin = max(tmin, t1)
                tmax = min(tmax, t2)
                if tmin > tmax:
                    return (False, None)
        return (True, tmin)
