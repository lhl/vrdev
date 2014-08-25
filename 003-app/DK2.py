#!/usr/bin/env python


from   OpenGL.arrays import vbo
from   OpenGL.GL import *
from   OpenGL.GL import shaders
import numpy
from   numpy import array
import pyglfw.pyglfw as fw
import sys


class DK2():
  def __init__(self, win):
    # glfw3 window
    self.win = win

    # bg
    self.bg = (0.0, 0.0, 1.0, 0.0)

    # this should go in an init function really
    # http://pyopengl.sourceforge.net/context/tutorials/shader_1.html
    VERTEX_SHADER = shaders.compileShader("""
      #version 120
      void main() {
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
      }
    """, GL_VERTEX_SHADER)

    FRAGMENT_SHADER = shaders.compileShader("""
      #version 120
      void main() {
        gl_FragColor = vec4( 0, 1, 0, 1 );
      }
    """, GL_FRAGMENT_SHADER)

    self.shader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)

    self.vbo = vbo.VBO(
      array( [
        [  0, 1, 0 ],
        [ -1,-1, 0 ],
        [  1,-1, 0 ],
        [  2,-1, 0 ],
        [  4,-1, 0 ],
        [  4, 1, 0 ],
        [  2,-1, 0 ],
        [  4, 1, 0 ],
        [  2, 1, 0 ],
      ],'f')
    )


  def render(self):
    glClearColor(*self.bg)
    glClear(GL_COLOR_BUFFER_BIT)

    shaders.glUseProgram(self.shader)
    try:
      self.vbo.bind()
      try:
        glEnableClientState(GL_VERTEX_ARRAY);
        glVertexPointerf(self.vbo)
        glDrawArrays(GL_TRIANGLES, 0, 9)
      finally:
        self.vbo.unbind()
        glDisableClientState(GL_VERTEX_ARRAY);
    finally:
      shaders.glUseProgram(0)

    # OK let's see what we got
    self.win.swap_buffers()
