#!/usr/bin/env python3

import matplotlib
import matplotlib.image
import numpy as np

import src.vec3 as vec3


if __name__ == '__main__':
    # (y, x, colors)
    out_shape = (100, 200, 3)
    # data = np.random.random(size=(256,256,3))

    data = np.zeros(shape=out_shape)

    # fill in with gradient
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            r = x / data.shape[0]
            g = y / data.shape[1]
            b = 0.0
            color = vec3.vec3(data=(r, g, b))
            data[x][y] = color.data


    matplotlib.image.imsave('out.png', data)


