#!/usr/bin/env python


import glfw
import ctypes
import numpy
from   numpy import array
from   OpenGL import GL, GLU
from   OpenGL.arrays import vbo
from   OpenGL.GL import shaders
from   OpenGL.raw.GL import _types
import PIL
from   PIL import Image
import sys
import time


class Window():
    def __init__(self, vs, fs, texture=None):
        self.loadShader(vs, fs)
        if texture:
            self.loadTexture(texture)


    def loadShader(self, vs, fs):
        VERTEX = open(vs).read()
        vertexShader = shaders.compileShader(VERTEX, GL.GL_VERTEX_SHADER)
        FRAGMENT = open(fs).read()
        fragmentShader = shaders.compileShader(FRAGMENT, GL.GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(vertexShader, fragmentShader)


    def loadTexture(self, texture):
        img = Image.open(texture).transpose(Image.FLIP_TOP_BOTTOM)
        img_data = numpy.fromstring(img.tobytes(), numpy.uint8)
        width, height = img.size

        # glTexImage2D expects the first element of the image data to be the
        # bottom-left corner of the image.  Subsequent elements go left to right,
        # with subsequent lines going from bottom to top.

        # However, the image data was created with PIL Image tostring and numpy's
        # fromstring, which means we have to do a bit of reorganization. The first
        # element in the data output by tostring() will be the top-left corner of
        # the image, with following values going left-to-right and lines going
        # top-to-bottom.  So, we need to flip the vertical coordinate (y). 
        self.texture = GL.glGenTextures(1)
        GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture)
        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR_MIPMAP_LINEAR)
        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, width, height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img_data)
        GL.glGenerateMipmap(GL.GL_TEXTURE_2D)

        # Free/Unbind
        GL.glBindTexture(GL.GL_TEXTURE_2D, 0);


class GLApp():
    def __init__(self):
        self.window = None
        self.VAO = None
        self.index_size = None


    def initialize(self):
        # Load Shader
        self.window = Window('007.vs', '007.frag', 'window.png')

        # Enable Transparency
        GL.glEnable(GL.GL_BLEND);
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA);


        # Same Data as EBO w/ Indices for buffers
        vertexData = numpy.array([
             # Positions       # Color         # Texture
             0.5,  0.5, 0.0,   1.0, 0.0, 0.0,  1.0, 1.0, # Top Right
             0.5, -0.5, 0.0,   0.0, 1.0, 0.0,  1.0, 0.0, # Bottom Right
            -0.5, -0.5, 0.0,   0.0, 0.0, 1.0,  0.0, 0.0, # Bottom Left
            -0.5,  0.5, 0.0,   1.0, 1.0, 0.0,  0.0, 1.0, # Top Left
        ], dtype=numpy.float32)

        indexData = numpy.array([
            0, 1, 2, # First Triangle
            0, 2, 3, # Second Triangle
        ], dtype=numpy.uint32)
        self.index_size = indexData.size

        # Core OpenGL requires that at least one OpenGL vertex array be bound
        self.VAO = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.VAO)

        # Need VBO for triangle vertices
        VBO = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, vertexData.nbytes, vertexData, GL.GL_STATIC_DRAW)

        # We make an EBO now
        EBO = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, EBO)
        GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, indexData.nbytes, indexData, GL.GL_STATIC_DRAW)

        # Define Stride
        stride = 8 * ctypes.sizeof(_types.GLfloat)

        # enable array and set up data - calculating stride length, wow; not documented
        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, stride, None)
        GL.glEnableVertexAttribArray(0)

        # I like how offsets aren't documented either; http://pyopengl.sourceforge.net/documentation/manual-3.0/glVertexAttribPointer.html
        # offsets https://twistedpairdevelopment.wordpress.com/2013/02/16/using-array_buffers-in-pyopengl/
        # http://stackoverflow.com/questions/11132716/how-to-specify-buffer-offset-with-pyopengl
        GL.glVertexAttribPointer(1, 3, GL.GL_FLOAT, GL.GL_FALSE, stride, ctypes.c_void_p((3 * ctypes.sizeof(_types.GLfloat))))
        GL.glEnableVertexAttribArray(1)

        GL.glVertexAttribPointer(2, 2, GL.GL_FLOAT, GL.GL_FALSE, stride, ctypes.c_void_p((6 * ctypes.sizeof(_types.GLfloat))))
        GL.glEnableVertexAttribArray(2)

        # Unbind so we don't mess w/ them
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glBindVertexArray(0)

        # Wireframe Mode
        # GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE);


    def render(self):
        GL.glClearColor(0, 0, 0, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        # active shader program
        GL.glUseProgram(self.window.shader)

        # Bind Texture
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.window.texture);

        try:
            GL.glBindVertexArray(self.VAO)
           
            # Draw a triangle
            # GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

            # draw triangle, starting index of the vertex array, # of vertices (6 = indexData.size), 
            # EBO indexes remain the same (accounts for stride of extra data
            GL.glDrawElements(GL.GL_TRIANGLES, self.index_size, GL.GL_UNSIGNED_INT, None)
        finally:
            # Unbind when we finish
            GL.glBindVertexArray(0)
            GL.glUseProgram(0)


    def run(self):
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
        # glfw.window_hint(glfw.RESIZABLE, 0)

        # These should work, but don't :(
        # could control focus w/ http://crunchbang.org/forums/viewtopic.php?id=22226
        # ended up using xdotool, see run.py
        glfw.window_hint(glfw.FOCUSED, 0)

        # I've set 'shader-*' to raise in openbox-rc as workaround
        # Looking at the code and confirming version 3.1.2 and it should work
        glfw.window_hint(glfw.FLOATING, 1)

        # Create a windowed mode window and its OpenGL context
        self.w = glfw.create_window(500, 500, "shader-test", None, None)
        if not self.w:
            glfw.terminate()
            return

        # Move Window
        glfw.set_window_pos(self.w, 1400, 50)

        # Callbacks
        glfw.set_key_callback(self.w, self.on_key)
        glfw.set_framebuffer_size_callback(self.w, self.on_resize);


        # Make the window's context current
        glfw.make_context_current(self.w)

        # vsync
        glfw.swap_interval(1)

        # Setup GL shaders, data, etc.
        self.initialize()

        # Loop until the user closes the window
        while not glfw.window_should_close(self.w):
            # Render here, e.g. using pyOpenGL
            self.render()

            # Swap front and back buffers
            glfw.swap_buffers(self.w)

            # Poll for and process events
            glfw.poll_events()

        glfw.terminate()

    
    # Callbacks
    def on_key(self, window, key, scancode, action, mods):
        print(key)
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window, 1)

    def on_resize(self, window, width, height):
        # optionally we can force aspect ratio

        GL.glViewport(0, 0, width, height)
        pass
    


if __name__ == "__main__":
    GLApp().run()
