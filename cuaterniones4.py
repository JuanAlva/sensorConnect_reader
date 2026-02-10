from pyquaternion import Quaternion
import math

my_quaternion = Quaternion(axis=[1, 0, 0], angle=3.14159265)

import numpy
numpy.set_printoptions(suppress=True) # Suppress insignificant values for clarity
v = numpy.array([0., 0., 1.]) # Unit vector in the +z direction
# v_prime = my_quaternion.rotate(v)

angle = 90
radian = math.radians(angle)
# print(radian)
# print(type(radian))
# print(type(3.14159265))
q1 = Quaternion(axis=[0, 0, 1], angle=radian) # Rotate 180 about X
q2 = Quaternion(axis=[0, 1, 0], angle=radian) # Rotate 90 about Y
q3 = q1 * q2 # Composite rotation of q1 then q2 expressed as standard multiplication
print(q3)

# from pyquaternion import Quaternion

# Definir dos rotaciones
# q1 = Quaternion(axis=[1, 0, 0], angle=0.1)
# q2 = Quaternion(axis=[0, 1, 0], angle=0.2)

# Composición de rotaciones usando @
q_combined = q1 @ q2
# print(q1,"\n",q2)
print(q_combined)

# q = q.normalised
