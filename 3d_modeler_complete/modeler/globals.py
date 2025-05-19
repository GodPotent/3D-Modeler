
from OpenGL.GL import *
from OpenGL.GLU import *

G_OBJ_SPHERE = 1
G_OBJ_CUBE = 2
G_OBJ_PLANE = 3

def init_primitives():
    glNewList(G_OBJ_SPHERE, GL_COMPILE)
    quad = gluNewQuadric()
    gluSphere(quad, 0.5, 32, 32)
    gluDeleteQuadric(quad)
    glEndList()

    glNewList(G_OBJ_CUBE, GL_COMPILE)
    glBegin(GL_QUADS)
    vertices = [
        # Left
        ((-0.5, -0.5, -0.5), (-0.5, -0.5,  0.5), (-0.5,  0.5,  0.5), (-0.5,  0.5, -0.5)),
        # Back
        ((-0.5, -0.5, -0.5), (-0.5,  0.5, -0.5), ( 0.5,  0.5, -0.5), ( 0.5, -0.5, -0.5)),
        # Right
        (( 0.5, -0.5, -0.5), ( 0.5,  0.5, -0.5), ( 0.5,  0.5,  0.5), ( 0.5, -0.5,  0.5)),
        # Front
        ((-0.5, -0.5,  0.5), ( 0.5, -0.5,  0.5), ( 0.5,  0.5,  0.5), (-0.5,  0.5,  0.5)),
        # Bottom
        ((-0.5, -0.5,  0.5), (-0.5, -0.5, -0.5), ( 0.5, -0.5, -0.5), ( 0.5, -0.5,  0.5)),
        # Top
        ((-0.5,  0.5, -0.5), (-0.5,  0.5,  0.5), ( 0.5,  0.5,  0.5), ( 0.5,  0.5, -0.5)),
    ]
    for face in vertices:
        for vertex in face:
            glVertex3f(*vertex)
    glEnd()
    glEndList()

    glNewList(G_OBJ_PLANE, GL_COMPILE)
    glBegin(GL_LINES)
    for i in range(-10, 11):
        glVertex3f(i, 0, -10)
        glVertex3f(i, 0, 10)
        glVertex3f(-10, 0, i)
        glVertex3f(10, 0, i)
    glEnd()
    glEndList()
