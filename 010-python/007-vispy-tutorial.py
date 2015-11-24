#!/usr/bin/env python

### AUTORELOAD
# python run.py to run autoreloader


### Imports
import sys
from   vispy import app, gloo
from   vispy.gloo import Program
from   vispy.gloo import gl


### VERTEX SHADER
vertex = """
#version 330 core

layout (location = 0) in vec3 position;

void main() {
  gl_Position = vec4(position.x, position.y, position.z, 1.0);
}
"""


### PIXEL/FRAGMENT SHADER
fragment = """
#version 330 core

out vec4 color;

void main() {
  color = vec4(1.0f, 0.5f, 0.2f, 1.0f);
}
"""


### COLOR
color = [
(1, 0, 0, 1), 
(0, 1, 0, 1),
(0, 0, 1, 1), 
(1, 1, 0, 1),
]


### POSITION - triangle_strip
position = [
(-1, -1), 
(-1, +1),
(+1, -1), 
(+1, +1),
]


### Vertex Buffer
vertices = [
(-0.5, -0.5, +0.0),
(+0.5, -0.5, +0.0),
(+0.0, +0.5, +0.0),
]  




### Basic App
class Canvas(app.Canvas):
  def __init__(self):
    app.Canvas.__init__(
      self, 
      always_on_top=True, 
      position=(1600,100), 
      size=(300, 300), 
      title='Colored quad', 
      keys='interactive'
    )
    # defaults to PyQt4
    # print(app.Application().backend_name)

    self.program = Program(vertex, fragment)

    self.program['a_position'] = gloo.VertexBuffer(vertices)

    self.program['u_color'] = 0.0, 1.0, 0.0

    # self.program['color'] = color 
    # self.program['position'] = position

    gloo.set_viewport(0, 0, *self.physical_size)
    self.show()

  def on_draw(self, event):
    # gloo.set_clear_color((0.2, 0.4, 0.6, 1.0))
    # gloo.clear()
    gloo.clear(color='black')

    self.program.draw(gl.GL_POINTS)
    # self.program.draw(gl.GL_TRIANGLES)
    # self.program.draw('triangle_strip')

  def on_resize(self, event):
    gloo.set_viewport(0, 0, *event.physical_size)


if __name__ == '__main__':
  c = Canvas()
  app.run()
