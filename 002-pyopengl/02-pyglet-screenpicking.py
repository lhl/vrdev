# coding: utf-8
import pyglet
from   pyglet import clock


window = pyglet.window.Window()
context = window.context
config = context.config

# We can do easy stereo rendering!
# config.stereo = 1


platform = pyglet.window.get_platform()
display = platform.get_default_display()
print display.get_screens()

# Set FPS
clock.set_fps_limit(75)
fps_display = clock.ClockDisplay()
fps_display.draw()
