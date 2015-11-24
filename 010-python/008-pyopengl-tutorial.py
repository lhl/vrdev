#!/usr/bin/env python


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


window = 0                                             # glut window number
window_size = (200, 200)
window_pos  = (1300, 100)


def draw():                                            # ondraw is called all the time
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
  glLoadIdentity()                                   # reset position
    
  # ToDo draw rectangle
    
  glutSwapBuffers()                                  # important for double buffering
    

# initialization
if __name__ == '__main__':
  glutInit()                                             # initialize glut
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
  glutInitWindowSize(window_size)                        # set window size
  glutInitWindowPosition(window_pos)                     # set window position
  window = glutCreateWindow("noobtuts.com")              # create window with title
  glutDisplayFunc(draw)                                  # set draw function callback
  glutIdleFunc(draw)                                     # draw all the time
  glutMainLoop()                                         # start everything
