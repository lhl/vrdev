#!/usr/bin/env python


import sys

import kivy
kivy.require('1.9.0')

from   kivy.app import App
from   kivy.clock import Clock
from   kivy.config import Config
from   kivy.core.window import Window
from   kivy.uix.floatlayout import FloatLayout
from   kivy.graphics import RenderContext
from   kivy.graphics.vertex_instructions import Triangle
from   kivy.properties import StringProperty, ObjectProperty


VERTEX = '''
#version 330 core
#ifdef GL_ES
  precision highp float;
#endif

in vec2 position;

void main()
{
  gl_Position = vec4(position, 0.0, 1.0);
}
'''

'''
/* Outputs to the fragment shader */
varying vec4 frag_color;
varying vec2 tex_coord0;

/* vertex attributes */
attribute vec2     vPosition;
attribute vec2     vTexCoords0;

/* uniform variables */
uniform mat4       modelview_mat;
uniform mat4       projection_mat;
uniform vec4       color;

'''


FRAGMENT = '''

#version 330 core
#ifdef GL_ES
  precision highp float;
#endif


uniform vec3 triangleColor;
out vec4 outColor;

void main()
{
  outColor = vec4(triangleColor, 1.0);
}
'''

'''
/* Outputs from the vertex shader */
varying vec4 frag_color;
varying vec2 tex_coord0;

/* uniform texture samplers */
uniform sampler2D texture0;

/* custom one */
uniform vec2 resolution;
uniform float time;

/* PLASMA SHADER
*/
void main(void)
{
   float x = gl_FragCoord.x;
   float y = gl_FragCoord.y;
   float mov0 = x+y+cos(sin(time)*2.)*100.+sin(x/100.)*1000.;
   float mov1 = y / resolution.y / 0.2 + time;
   float mov2 = x / resolution.x / 0.2;
   float c1 = abs(sin(mov1+time)/2.+mov2/2.-mov1-mov2+time);
   float c2 = abs(sin(c1+sin(mov0/1000.+time)
              +sin(y/40.+time)+sin((x+y)/100.)*3.));
   float c3 = abs(sin(c2+cos(mov1+mov2+c2)+cos(mov2)+sin(x/1000.)));
   gl_FragColor = vec4( c1,c2,c3,1.0);
}
'''




"""
class ShaderViewer(FloatLayout):
    fs = StringProperty(None)
    vs = StringProperty(None)

    def __init__(self, **kwargs):
        self.canvas = RenderContext()
        super(ShaderViewer, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_shader, 0)

    def update_shader(self, *args):
        s = self.canvas
        s['projection_mat'] = Window.render_context['projection_mat']
        s['time'] = Clock.get_boottime()
        s['resolution'] = list(map(float, self.size))
        s.ask_update()

    def on_fs(self, instance, value):
        self.canvas.shader.fs = value

    def on_vs(self, instance, value):
        self.canvas.shader.vs = value

Factory.register('ShaderViewer', cls=ShaderViewer)


class ShaderEditor(FloatLayout):

    source = StringProperty('data/logo/kivy-icon-512.png')

    fs = StringProperty('''
void main (void){
    gl_FragColor = frag_color * texture2D(texture0, tex_coord0);
}
''')
    vs = StringProperty('''
void main (void) {
  frag_color = color;
  tex_coord0 = vTexCoords0;
  gl_Position = projection_mat * modelview_mat * vec4(vPosition.xy, 0.0, 1.0);
}
''')

    viewer = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ShaderEditor, self).__init__(**kwargs)
        self.test_canvas = RenderContext()
        s = self.test_canvas.shader
        self.trigger_compile = Clock.create_trigger(self.compile_shaders, -1)
        self.bind(fs=self.trigger_compile, vs=self.trigger_compile)

    def compile_shaders(self, *largs):
        print('try compile')
        if not self.viewer:
            return
        fs = fs_header + self.fs
        vs = vs_header + self.vs
        print('-->', fs)
        self.viewer.fs = fs
        print('-->', vs)
        self.viewer.vs = vs


class ShaderEditorApp(App):
    def build(self):
        kwargs = {}
        if len(sys.argv) > 1:
            kwargs['source'] = sys.argv[1]
        return ShaderEditor(**kwargs)

if __name__ == '__main__':
    ShaderEditorApp().run()
"""


class ShaderWidget(FloatLayout):
  # property to set the source code for shaders
  vs = StringProperty(None)
  fs = StringProperty(None)

  def __init__(self, **kwargs):
    # Instead of using Canvas, we will use a RenderContext,
    # and change the default shader used.
    self.canvas = RenderContext()

    # Add a Triangle
    self.triangle = Triangle(points=[0,0, 100,100, 200,0])

    # call the constructor of parent
    # if they are any graphics object, they will be added on our new canvas
    super(ShaderWidget, self).__init__(**kwargs)

    # We'll update our glsl variables in a clock
    Clock.schedule_interval(self.update_glsl, 1 / 60.)

  def on_fs(self, instance, value):
    # set the fragment shader to our source code
    shader = self.canvas.shader
    old_value = shader.fs
    shader.fs = value
    if not shader.success:
      shader.fs = old_value
      raise Exception('failed')

  def on_vs(self, instance, value):
    # set the fragment shader to our source code
    shader = self.canvas.shader
    old_value = shader.vs
    shader.vs = value
    if not shader.success:
      shader.vs = old_value
      raise Exception('failed')

  def update_glsl(self, *largs):
    self.canvas['time'] = Clock.get_boottime()
    self.canvas['resolution'] = list(map(float, self.size))
    # This is needed for the default vertex shader.
    self.canvas['projection_mat'] = Window.render_context['projection_mat']

  def on_move(self):
    print('moved')


class ShaderApp(App):
  def build(self):
    def save(self):
      print('---')
      print(self._win.win)
      print('---')
      Config.set('graphics', 'height', self.size[0])
      Config.set('graphics', 'width', self.size[1])
      Config.set('graphics', 'top', self.top)
      Config.set('graphics', 'left', self.left)
      Config.write()
    Window.bind(on_close=save)

    return ShaderWidget(fs=FRAGMENT, vs=VERTEX)


if __name__ == '__main__':
  ShaderApp().run()
