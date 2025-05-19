
import sys
import numpy as np
from modeler.nodes import Cube, Sphere, SnowFigure
from modeler.geometry import normalize
from modeler.geometry import AABB

class Scene:
    PLACE_DEPTH = 15.0

    def __init__(self):
        self.node_list = []
        self.selected_node = None

    def add_node(self, node):
        self.node_list.append(node)

    def render(self):
        for node in self.node_list:
            node.render()

    def pick(self, start, direction, modelview):
        if self.selected_node:
            self.selected_node.select(False)
            self.selected_node = None

        min_dist = sys.maxsize
        closest = None
        for node in self.node_list:
            hit, dist = node.pick(start, direction, modelview)
            if hit and dist < min_dist:
                min_dist = dist
                closest = node

        if closest:
            closest.select(True)
            closest.depth = min_dist
            closest.selected_loc = start + direction * min_dist
            self.selected_node = closest

    def move_selected(self, start, direction, inverse_modelview):
        if not self.selected_node:
            return
        node = self.selected_node
        old_loc = node.selected_loc
        new_loc = start + direction * node.depth
        translation = new_loc - old_loc
        pre_tran = np.array([translation[0], translation[1], translation[2], 0])
        world_tran = inverse_modelview.dot(pre_tran)

        node.translate(world_tran[0], world_tran[1], world_tran[2])
        node.selected_loc = new_loc

    def rotate_selected_color(self, forward=True):
        if self.selected_node:
            self.selected_node.rotate_color(forward)

    def scale_selected(self, up=True):
        if self.selected_node:
            self.selected_node.scale(up)

    def place(self, shape, start, direction, inverse_modelview):
        if shape == 'cube':
            node = Cube()
        elif shape == 'sphere':
            node = Sphere()
        elif shape == 'figure':
            node = SnowFigure()
        else:
            return

        self.add_node(node)

        translation = start + direction * self.PLACE_DEPTH
        pre_tran = np.array([translation[0], translation[1], translation[2], 1])
        world_tran = inverse_modelview.dot(pre_tran)

        node.translate(world_tran[0], world_tran[1], world_tran[2])
