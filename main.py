#!/usr/bin/env python3

import matplotlib
import matplotlib.image
import numpy as np

# include local libraries
from src.vec3 import vec3
from src.ray import ray


def hit_sphere(center, radius, r):
    '''check for sphere intersection'''
    oc = r.origin - center
    a = r.direction.dot(r.direction)
    b = 2.0 * oc.dot(r.direction)
    c = oc.dot(oc) - radius**2
    discriminant = b**2 - 4 * a * c
    return discriminant > 0

def skybox_color(r):
    '''simple skybox function'''
    if hit_sphere(vec3((0.0, 0.0, -1.0)), 0.5, r):
        return vec3((1.0, 0.0, 0.0))
    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y() + 1.0)
    return vec3((1.0, 1.0, 1.0))*(1.0-t) + vec3((0.5, 0.7, 1.0))*t

if __name__ == '__main__':
    # (y, x, colors)
    out_shape = (100, 200, 3)
    # data = np.random.random(size=(256,256,3))
    # initialize as black
    data = np.zeros(shape=out_shape)

    # camera parameters
    lower_left_corner = vec3((-2.0, -1.0, -1.0))
    horizontal = vec3((4.0, 0.0, 0.0))
    vertical = vec3((0.0, 2.0, 0.0))
    origin = vec3((0.0, 0.0, 0.0))

    # fill in image
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            u = x / data.shape[1]
            v = y / data.shape[0]
            r = ray(origin = origin, direction = lower_left_corner + horizontal * u + vertical * v)
            color = skybox_color(r)
            # flip y to match book
            data[data.shape[0] - y - 1][x] = color.data

    # save to file
    matplotlib.image.imsave('out.png', data)


