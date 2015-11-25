#!/usr/bin/env python
"""Quick hack of 'modern' OpenGL example using pysdl2 and pyopengl

Implementation of:
http://www.learnopengl.com/#!Getting-started/Hello-Triangle

Compare to
https://github.com/neutralord/pyopengl-experiments/blob/master/red_book_samples/uniform.py
https://github.com/neutralord/pyopengl-experiments

http://schi.iteye.com/blog/1969710
"""

import glfw
import sys
import ctypes
import numpy

from OpenGL import GL, GLU
from OpenGL.GL import shaders
from OpenGL.arrays import vbo

from numpy import array

shaderProgram = None
VAO = None
VBO = None

### VERTEX SHADER
VERTEX = """
#version 330

layout (location = 0) in vec3 position;

void main()
{
  gl_Position = vec4(position.x, position.y, position.z, 1.0);
}
"""

### FRAGMENT SHADER
FRAGMENT = """
#version 330

out vec4 color;

void main()
{
  color = vec4(1.0f, 0.5f, 0.2f, 1.0f);
}
"""


def initialize():
    global shaderProgram
    global VAO
    global VBO

    vertexShader = shaders.compileShader(VERTEX, GL.GL_VERTEX_SHADER)

    fragmentShader = shaders.compileShader(FRAGMENT, GL.GL_FRAGMENT_SHADER)

    shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)


    # Vertex Data in an array - in Normalized Device Coordinates (NDC)
    vertexData = numpy.array([
	# Vertex Positions - Clockwise
        -0.5, -0.5, 0.0, # Left
         0.5, -0.5, 0.0, # Right
         0.0,  0.5, 0.0, # Top 
    ], dtype=numpy.float32)

    # Core OpenGL requires that at least one OpenGL vertex array be bound
    VAO = GL.glGenVertexArrays(1) # id:1
    GL.glBindVertexArray(VAO)

    # Need VBO for triangle vertices
    VBO = GL.glGenBuffers(1) # id:1
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, vertexData.nbytes, vertexData,
        GL.GL_STATIC_DRAW)

    # enable array and set up data
    GL.glEnableVertexAttribArray(0)
    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0,
        None)

    # Unbind so we don't mess w/ them
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
    GL.glBindVertexArray(0)


def render():
    global shaderProgram
    global VAO
    GL.glClearColor(0, 0, 0, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    # active shader program
    GL.glUseProgram(shaderProgram)

    try:
        GL.glBindVertexArray(VAO)

        # draw triangle, starting index of the vertex array, # of vertices
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
    finally:
        # Unbind when we finish
        GL.glBindVertexArray(0)
        GL.glUseProgram(0)


def main():
    # Initialize the library
    if not glfw.init():
        return

    # Set some window hints
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3);
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3);
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE);
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE);
    glfw.window_hint(glfw.SAMPLES, 16)

    # This works as expected
    glfw.window_hint(glfw.RESIZABLE, 0)

    # These should work, but don't :(
    # could control focus w/ http://crunchbang.org/forums/viewtopic.php?id=22226
    # ended up using xdotool, see run.py
    glfw.window_hint(glfw.FOCUSED, 0)

    # I've set 'shader-*' to raise in openbox-rc as workaround
    # Looking at the code and confirming version 3.1.2 and it should work
    glfw.window_hint(glfw.FLOATING, 1)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(300, 300, "shader-test", None, None)
    if not window:
        glfw.terminate()
        return

    # Move Window
    glfw.set_window_pos(window, 1600, 50)

    # Make the window's context current
    glfw.make_context_current(window)

    # vsync
    glfw.swap_interval(1)

    # Setup GL shaders, data, etc.
    initialize()

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        render()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
