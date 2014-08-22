#!/usr/bin/env python


import pyglfw.pyglfw as glfw


def main():
  # Initialize
  glfw.init()

  # Monitor Info
  # print_all_monitors()


def print_all_monitors():
  '''
  note you can run xrandr in the command line to get the info as well
  rift will look like:

  DP-0 connected primary 1920x1080+0+0 left (normal left inverted right x axis y axis) 71mm x 126mm
    1080x1920      75.0*+   72.0     60.0  
    1080x948      120.0  

  '''
  print
  for monitor in glfw.get_monitors():
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
  for monitor in glfw.get_monitors():
    if monitor.physical_size == (71, 126):
      return monitor

  ### TODO: DK1 physical size

  # If we're still here (no rift?), lets just return the primary display
  return glfw.get_primary_monitor()
  



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
