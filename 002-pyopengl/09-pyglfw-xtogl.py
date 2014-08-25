#!/usr/bin/env python


from   OpenGL.arrays import vbo
from   OpenGL.GL import *
from   OpenGL.GL import shaders
from   OpenGL.GLX import *
import numpy
from   numpy import array
import pyglfw.pyglfw as fw
import sys
from   Xlib.display import Display


def main():
  ### Initialize
  fw.init()

  ### Rift
  monitor = get_rift()

  win = CbWindow(640, 480, 'pyglfw')
  win.make_current()

  # XWindows...
  d = Display()
  root = d.screen().root
  pixmap = root.create_pixmap(256, 256, 8)
  # glXCreateWindow(d, cfg, pixmap, 0)


  while not win.should_close:

    render()

    win.swap_buffers()
    fw.poll_events()

    if win.keys.escape:
        win.should_close = True

  fw.terminate()


def render():
  # blue bg
  blue = (0.0, 0.0, 1.0, 0.0)
  glClearColor(*blue)
  glClear(GL_COLOR_BUFFER_BIT)

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

  shader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)

  myvbo = vbo.VBO(
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

  shaders.glUseProgram(shader)
  try:
    myvbo.bind()
    try:
      glEnableClientState(GL_VERTEX_ARRAY);
      glVertexPointerf(myvbo)
      glDrawArrays(GL_TRIANGLES, 0, 9)
    finally:
      myvbo.unbind()
      glDisableClientState(GL_VERTEX_ARRAY);
  finally:
    shaders.glUseProgram(0)


class DK2():
  def __init__(self):
    pass








def on_monitor(_monitor, _event):
  change_markers = {fw.Monitor.CONNECTED: '+', fw.Monitor.DISCONNECTED: '-'}
  change = change_markers.get(_event, '~')
  print("screen: %s %s" % (change, _monitor.name))





class CbWindow(fw.Window):
  def __init__(self, *args, **kwargs):
    super(CbWindow, self).__init__(*args, **kwargs)

    self.set_key_callback(CbWindow.key_callback)
    self.set_char_callback(CbWindow.char_callback)
    self.set_scroll_callback(CbWindow.scroll_callback)
    self.set_mouse_button_callback(CbWindow.mouse_button_callback)
    self.set_cursor_enter_callback(CbWindow.cursor_enter_callback)
    self.set_cursor_pos_callback(CbWindow.cursor_pos_callback)
    self.set_window_size_callback(CbWindow.window_size_callback)
    self.set_window_pos_callback(CbWindow.window_pos_callback)
    self.set_window_close_callback(CbWindow.window_close_callback)
    self.set_window_refresh_callback(CbWindow.window_refresh_callback)
    self.set_window_focus_callback(CbWindow.window_focus_callback)
    self.set_window_iconify_callback(CbWindow.window_iconify_callback)
    self.set_framebuffer_size_callback(CbWindow.framebuffer_size_callback)

  def key_callback(self, key, scancode, action, mods):
    print(
      "keybrd: key=%s scancode=%s action=%s mods=%s" %
      (key, scancode, action, mods))

  def char_callback(self, char):
    print("unichr: char=%s" % char)

  def scroll_callback(self, off_x, off_y):
    print("scroll: x=%s y=%s" % (off_x, off_y))

  def mouse_button_callback(self, button, action, mods):
    print("button: button=%s action=%s mods=%s" % (button, action, mods))

  def cursor_enter_callback(self, status):
    print("cursor: status=%s" % status)

  def cursor_pos_callback(self, pos_x, pos_y):
    print("curpos: x=%s y=%s" % (pos_x, pos_y))

  def window_size_callback(self, wsz_w, wsz_h):
    print("window: w=%s h=%s" % (wsz_w, wsz_h))

  def window_pos_callback(self, pos_x, pos_y):
    print("window: x=%s y=%s" % (pos_x, pos_y))

  def window_close_callback(self):
    print("should: %s" % self.should_close)

  def window_refresh_callback(self):
    print("redraw")

  def window_focus_callback(self, status):
    print("active: status=%s" % status)

  def window_iconify_callback(self, status):
    print("hidden: status=%s" % status)

  def framebuffer_size_callback(self, fbs_x, fbs_y):
    print("buffer: x=%s y=%s" % (fbs_x, fbs_y))

  ### Swap
  # window.swap_interval(0)
  # window.make_current()
  # window.swap_buffers()



def print_all_monitors():
  '''
  note you can run xrandr in the command line to get the info as well
  rift will look like:

  DP-0 connected primary 1920x1080+0+0 left (normal left inverted right x axis y axis) 71mm x 126mm
    1080x1920      75.0*+   72.0     60.0  
    1080x948      120.0  

  '''
  print
  for monitor in fw.get_monitors():
    print monitor.name
    print monitor.physical_size
    print monitor.pos
    for mode in monitor.video_modes:
      print '  mode:'
      print '    %s' % mode.width
      print '    %s' % mode.height
      print '    %s' % mode.refresh_rate
    print


def get_rift():
  '''
  http://unix.stackexchange.com/questions/67983/get-monitor-make-and-model-and-other-info-in-human-readable-form
  http://superuser.com/questions/800572/interpret-edid-information-to-get-manufacturer-and-type-number-of-my-laptop-scre
  http://ubuntuforums.org/showthread.php?t=1946208
  https://github.com/glfw/glfw/issues/212

  If we could easily read the EDID that'd be much easier
  Vendor is OVR

  read-edid barfs w/ Nvida (maybe can use NV-CONTROL)

  xrandr --verbose works...
  '''

  # For now, lets do the easiest thing and get it by physical size of DK2
  for monitor in fw.get_monitors():
    if monitor.physical_size == (71, 126):
      return monitor

  ### TODO: DK1 physical size

  # If we're still here (no rift?), lets just return the primary display
  return fw.get_primary_monitor()
  



'''
# If a new monitor is connected...
def on_monitor_event(monitor, event):
  if event == glfw.Monitor.CONNECTED:
    print(monitor.name)

glfw.Monitor.set_callback(on_monitor_event)


# Hints
glfw.Window.hint()
glfw.Window.hint(client_api=glfw.Window.OPENGL_API)
w, h = curmode.width, curmode.height
window = glfw.Window(w, h, 'pyglfw')
window.close()

GLFW_STEREO   GL_FALSE  GL_TRUE or GL_FALSE
The GLFW_STEREO hint specifies whether to use stereoscopic rendering.

GLFW_REFRESH_RATE   0   0 to INT_MAX
The GLFW_REFRESH_RATE hint specifies the desired refresh rate for full screen windows. If set to zero, the highest available refresh rate will be used. This hint is ignored for windowed mode windows.

# Swap
# makes context current
# and restores previous
window.swap_interval(0)
window.make_current()
window.swap_buffers()


# Windows
if not window.should_close:
  window.set_title('pyglfw')
  size = window.size
  window.show()
is_visible = window.visible
client_api = window.client_api
window.has_focus = True

def on_window_size(window, w, h):
  window.size = size

window.set_window_size_callback(on_window_size)


# Inputs
mode = window.sticky_keys
window.sticky_mice = mode
is_escape = window.keys.escape
is_middle = window.mice.middle
cursor_at = window.cursor_pos

def on_key(window, key, scancode, action, mods):
  if key == glfw.Keys.ESCAPE:
    window.should_close = True

window.set_key_callback(on_key)

js = glfw.Joystick(0)

if js:
  joy_name = js.name
  joy_axes = js.axes
'''

if __name__ == '__main__':
  main()
