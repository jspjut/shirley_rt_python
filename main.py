#!/usr/bin/env python3

import matplotlib
import matplotlib.image
import numpy as np

# data = np.random.random(size=(256,256,3))

data = np.zeros(shape=(256,256,3))



matplotlib.image.imsave('out.png', data)


