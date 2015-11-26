#!/usr/bin/env python

from pyrr import Quaternion, Matrix44, Vector3
import numpy as np

# Translation
point = Vector3([1.0, 0.0, 0.0])
print('point: %s' % point)
point += [1.0, 1.0, 0.0]
print('translated: %s' % point)



# rotate about Y by pi/2
rotation = Quaternion.from_y_rotation(np.pi / 2.0)
orientation = rotation * orientation

'''
rotate()
setangletoworld()
setangletocamera()

move()
moveto()

lerp



'''
