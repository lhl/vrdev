#!/usr/bin/env python

import sys
from   vispy import app, gloo
from   vispy.gloo import Program

vertex = """
    attribute vec4 color;
    attribute vec2 position;
    varying vec4 v_color;

    void main() {
      gl_Position = vec4(position, 0.0, 1.0);
      v_color = color;
    }
"""

fragment = """
  varying vec4 v_color;
  void main() {
    gl_FragColor = v_color;
  }
"""

class Canvas(app.Canvas):
  def __init__(self):
    app.Canvas.__init__(self, size=(800, 800), title='Colored quad', keys='interactive')

    self.program = Program(vertex, fragment, count=4)
    self.program['color'] = [
      (1, 0, 0, 1), 
      (0, 1, 0, 1),
      (0, 0, 1, 1), 
      (1, 1, 0, 1)
    ]
    self.program['position'] = [
      (-1, -1), 
      (-1, +1),
      (+1, -1), 
      (+1, +1)
    ]
    gloo.set_viewport(0, 0, *self.physical_size)
    self.show()

  def on_draw(self, event):
    # gloo.set_clear_color((0.2, 0.4, 0.6, 1.0))
    # gloo.clear()
    gloo.clear(color='white')
    self.program.draw('triangle_strip')

  def on_resize(self, event):
    gloo.set_viewport(0, 0, *event.physical_size)


if __name__ == '__main__':
  c = Canvas()
  app.run()
