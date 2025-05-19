
import numpy as np
import random
from OpenGL.GL import *

from modeler.geometry import translation, scaling, AABB
from modeler import colors
from modeler.globals import G_OBJ_SPHERE, G_OBJ_CUBE

class Node:
    def __init__(self):
        self.color_index = random.randint(colors.MIN_COLOR, colors.MAX_COLOR)
        self.translation_matrix = np.identity(4)
        self.scaling_matrix = np.identity(4)
        self.aabb = AABB([0.0, 0.0, 0.0], [0.5, 0.5, 0.5])
        self.selected = False

    def render(self):
        glPushMatrix()
        glMultMatrixf(np.transpose(self.translation_matrix))
        glMultMatrixf(self.scaling_matrix)

        r, g, b = colors.COLORS[self.color_index]
        glColor3f(r, g, b)

        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.3, 0.3, 0.3])
        self.render_self()
        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0])

        glPopMatrix()

    def pick(self, start, direction, mat):
        newmat = np.dot(np.dot(mat, self.translation_matrix), np.linalg.inv(self.scaling_matrix))
        return self.aabb.ray_hit(start, direction, newmat)

    def translate(self, x, y, z):
        self.translation_matrix = np.dot(self.translation_matrix, translation([x, y, z]))

    def scale(self, up):
        s = 1.1 if up else 0.9
        self.scaling_matrix = np.dot(self.scaling_matrix, scaling([s, s, s]))
        self.aabb.scale(s)

    def select(self, select=None):
        if select is not None:
            self.selected = select
        else:
            self.selected = not self.selected

    def rotate_color(self, forward=True):
        self.color_index += 1 if forward else -1
        if self.color_index > colors.MAX_COLOR:
            self.color_index = colors.MIN_COLOR
        if self.color_index < colors.MIN_COLOR:
            self.color_index = colors.MAX_COLOR

    def render_self(self):
        raise NotImplementedError("Abstract Node doesn't implement 'render_self'")

class Primitive(Node):
    def __init__(self):
        super().__init__()
        self.call_list = None

    def render_self(self):
        glCallList(self.call_list)

class Cube(Primitive):
    def __init__(self):
        super().__init__()
        self.call_list = G_OBJ_CUBE

class Sphere(Primitive):
    def __init__(self):
        super().__init__()
        self.call_list = G_OBJ_SPHERE

class HierarchicalNode(Node):
    def __init__(self):
        super().__init__()
        self.child_nodes = []

    def render_self(self):
        for child in self.child_nodes:
            child.render()

class SnowFigure(HierarchicalNode):
    def __init__(self):
        super().__init__()
        self.child_nodes = [Sphere(), Sphere(), Sphere()]
        self.child_nodes[0].translate(0, -0.6, 0)
        self.child_nodes[1].translate(0, 0.1, 0)
        self.child_nodes[1].scaling_matrix = np.dot(self.scaling_matrix, scaling([0.8, 0.8, 0.8]))
        self.child_nodes[2].translate(0, 0.75, 0)
        self.child_nodes[2].scaling_matrix = np.dot(self.scaling_matrix, scaling([0.7, 0.7, 0.7]))
        for node in self.child_nodes:
            node.color_index = colors.MIN_COLOR
        self.aabb = AABB([0.0, 0.0, 0.0], [0.5, 1.1, 0.5])
