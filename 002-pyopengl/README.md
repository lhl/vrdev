PyOpenGL
---
* Low Level, useful, but probably won't need it.
* GLUT is old and crusty. Let's not use that. It also has no idea how to pick from multiple monitors


Pyglet
---
Pyglet isn't super active but does most of what we want. It can address multiple monitors (but not get attributes besides resolution), supports shaders, etc.

https://code.google.com/p/pyglet-shaders/
http://www.pythonstuff.org/glsl/example_2_glsl_with_pyglet.html
http://stackoverflow.com/questions/16003704/pyglet-shaders-and-glsl-layout-tag-for-color-attribute
http://codeflow.org/entries/2009/jul/31/gletools-advanced-pyglet-utilities/


GLFW
---
Not super pythonic, but maybe the best option? It's very active and supports all kinds of stuff (lots of good monitor stuff)

http://www.glfw.org/docs/latest/monitor.html
https://github.com/glfw/glfw
https://pypi.python.org/pypi/glfw/1.0.1
https://github.com/FlorianRhiem/pyGLFW
https://github.com/rougier/pyglfw

Install: 
use PPA:
https://launchpad.net/~keithw/+archive/ubuntu/glfw3

or 
http://stackoverflow.com/questions/17768008/how-to-build-install-glfw-3-and-use-it-in-a-linux-project

in utopic:
http://packages.ubuntu.com/source/utopic/powerpc/glfw3


PyGLy
---
This looks pretty useful, worth a poke around for helpers

https://github.com/adamlwgriffiths/PyGLy
https://groups.google.com/forum/#!topic/pyglet-users/9LDt7MlOxBI



vsync

Apply Distortion Shader
Shader
https://github.com/elect86/JavaOculusRoomTiny/tree/master/src/roomTinySimplified

https://github.com/OculusRiftInAction/OculusRiftInAction/tree/master/examples/webgl

http://schi.iteye.com/blog/1969710
