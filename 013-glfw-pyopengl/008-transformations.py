#!/usr/bin/env python

import pyrr
from   pyrr import Quaternion, Matrix44, Vector3
import numpy as np
import sys

# Translation
'''
point = Vector3([1.0, 0.0, 0.0])
print('point: %s' % point)
point += [1.0, 1.0, 0.0]
print('translated: %s' % point)
'''

# Rotate and then Scale
deg = 90.0
rad = np.radians(deg)

v = Vector3([0.0, 0.0, 1.0])
scale = Vector3([0.5, 0.5, 0.5])
print('Original: %s' % v)

# Rotate
rotate_mat4 = pyrr.matrix44.create_from_axis_rotation([0.0, 0.0, 1.0], rad)
v = Matrix44(rotate_mat4) * v
print('Rotate: %s' % v)

v = Matrix44().from_scale(scale) * v
print('Scale: %s' % v)

# array([[ -1.13698227e+002,   4.25087011e-303],
#         |         [  2.88528414e-306,   3.27025015e-309]])



# rotate about Y by pi/2
# rotation = Quaternion.from_y_rotation(np.pi / 2.0)
# orientation = rotation * orientation

'''
rotate()
setangletoworld()
setangletocamera()

move()
moveto()

lerp



'''
