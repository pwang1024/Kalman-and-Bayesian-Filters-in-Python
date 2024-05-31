
import os
import sys
sys.path.insert(0,os.getcwd()) 

import numpy as np
from filterpy.gh import GHFilter

# Create a basic filter for a scalar value with g=.8, h=.02.
# Initialize to 0, with a derivative(velocity) of 0.
f1_1      = GHFilter (x=0., dx=0., dt=1., g=.8, h=.02)
result1_1 = f1_1.update(z=1)
print(result1_1)

f1_2      = GHFilter (x=1., dx=0., dt=1., g=.8, h=.02)
result1_2 = f1_2.update(z=5)
print(result1_2)

# Create a filter with two independent variables.
f2_1      = GHFilter (x=np.array([0,1]), dx=np.array([0,0]), dt=1, g=.8, h=.02)
result2_1 = f2_1.update(np.array([1,5]))
print(result2_1)
print('done')