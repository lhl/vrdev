from wasabisg.scenegraph import Scene

scene = Scene(
        ambient=(0.05, 0.05, 0.05, 1.0)
)

'''
from wasabisg.loaders.objloader import ObjFileLoader
from wasabisg.scenegraph import ModelNode

loader = ObjFileLoader()
tree_model = loader.load_obj('tree.obj')

tree = ModelNode(tree_model, pos=(10, 0, 10))
scene.add(tree)
'''

from wasabisg.lighting import Light

# Distant light to approximate the sun
sunlight = Light(
  pos=(100, 100, 100),
  colour=(1.0, 1.0, 1.0, 1.0),
  intensity=10,
  falloff=0
)
scene.add(sunlight)

from euclid import Point3
from wasabisg.scenegraph import Camera

c = Camera(
  pos=Point3(0, 1, -20),
  look_at=(0, 1, 0),
  width=800,  # or whatever size your viewport is
  height=600
)

scene.render(c)
