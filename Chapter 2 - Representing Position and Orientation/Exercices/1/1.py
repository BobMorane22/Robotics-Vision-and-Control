#==================================================================================================
# Robotics, Vision and Control (Third Edition)
#
# Chapter 2 : Representing Position and Orientation
# Exercice  : 1
#--------------------------------------------------------------------------------------------------

# SETUP
# -------------------------------------------------------------------------------------------------
from spatialmath.base import *
from spatialmath import *

import matplotlib
import numpy

# Allow using Mathplotlib in non-interactive mode (i.e from scripts).
matplotlib.pyplot.ioff();


# EXERCISE
# -------------------------------------------------------------------------------------------------
theta = 0.4;
v0_0  = numpy.array([1, 1]);

# First, we plot the world frame {0} (in black). Then we
# plot the frame {A} (in blue).
plotvol2([-0.5, 1.5], grid=True);
T_0 = transl2(0, 0);
T_0A = rot2(theta);
trplot2(T_0, frame="0", color="k");
trplot2(T_0A, frame="A", color="b");

# We plot vector v0, with respect to the frame {0} (in red).
plot_arrow((0, 0), v0_0, label="$\overrightarrow{^0v_0}$", color='r', width=0.01)

# By applying the rotation matrix T_0A to v0_0, we rotate this
# vector by the same angle which rotated frame {0} into frame
# {A}. We call this vector va. Note that the coordinates of va
# at this point are still expressed with respect to the world
# frame. We plot this vector in green.
va_0 = T_0A @ v0_0;
print(f"va_0 = {va_0}");

plot_arrow((0, 0), va_0, label="$\overrightarrow{^0v_a}$", color='g', width=0.01)
matplotlib.pyplot.show();

# (EXTRA) We express the vector v0_0 in the frame {A}:
# We have that, from (2.13):
#
#                   v0_0 = T_0A * v0_A
#
# We can isolate va_0 by multiplying by T_0Ainv on each side:
#
#           T_0A⁻¹ * v0_0 = T_0A⁻¹ * T_0A * v0_A
#           T_0A⁻¹ * v0_0 = v0_A
#
# or:
#
#                    v0_A = T_0A⁻¹ * v0_0
#
T_0Ainv = numpy.linalg.inv(T_0A);
v0_A = T_0Ainv @ v0_0;
print(f"v0_A = {v0_A}");

# Effect of multiplication with its inverse matrix:
trplot2(T_0A @ T_0Ainv, color="k");
trplot2(T_0Ainv @ T_0A, color="b");
matplotlib.pyplot.show();

# In both cases, the multiplication with the inverse
# yields the identity matrix.

# Both determinants yield 1, since both are rotation
# matrices.
print(f"det(T_0A) = {numpy.linalg.det(T_0A)}");
print(f"det(T_0Ainv) = {numpy.linalg.det(T_0Ainv)}");
