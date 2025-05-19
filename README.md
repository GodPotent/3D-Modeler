
# 3D Modeler (Based on '500 Lines or Less')

A compact, educational 3D modeling tool using Legacy OpenGL and Python. Based on Erick Dransch's original concept from the [500 Lines or Less](https://aosabook.org/en/500L/) project.

## Features
- Place and manipulate primitive shapes (Cubes, Spheres)
- Hierarchical scene graph using nodes
- Scene rotation, translation, and scaling via mouse
- Interactive selection and movement of objects
- OpenGL + GLUT rendering (Legacy OpenGL)

## Requirements
- Python 3.7+
- PyOpenGL
- NumPy

## Installation

```bash
pip install PyOpenGL PyOpenGL_accelerate numpy
```

## Usage

```bash
python main.py
```

## Controls
- Left-click: Select and move object
- Right-click drag: Rotate view
- Scroll wheel: Zoom
- `C`: Place cube
- `S`: Place sphere
- Arrow keys: Change color / scale object

## License
MIT
