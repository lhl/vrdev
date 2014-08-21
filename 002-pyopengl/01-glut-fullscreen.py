#!/usr/bin/env python

'''
http://excid3.com/blog/python-and-opengl-game-mode-on-dual-monitors-tutorial/
http://python-catalin.blogspot.de/2011/08/creating-fullscreen-applications.html
'''

import sys
from   OpenGL.GL import *
from   OpenGL.GLUT import *

def main():
 
    # Initialize OpenGL
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

 
    # Configure the display output
    glutGameModeString("1920x1080:32@75")

    # The application will enter fullscreen
    glutEnterGameMode()
 
    # Setup callbacks for keyboard and display
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
 
    # Enters the GLUT event processing loop
    glutMainLoop()
 

def keyboard(key, x, y):
    if key == 'q':
        sys.exit(0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a green line
    glBegin(GL_LINES)
    glColor3f(0.0,100.0,0.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()
 
    glutSwapBuffers()
 
if __name__ == "__main__":
    main()
