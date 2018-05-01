#!/usr/bin/env python3

import matplotlib
import matplotlib.image
import numpy as np
import time

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
    # return the solution to the quadratic function if real, otherwise t = -1, which is behind camera
    return np.where((discriminant>0), (0.0-b - np.sqrt(discriminant)) / (a * 2.0), -1.0)

def skybox_color(r):
    '''simple skybox function'''
    t = hit_sphere(vec3((0.0, 0.0, -1.0)), 0.5, r)
    # if valid hit (t > 0.0)
    N = (r.point_at_parameter(t) - vec3((0.0, 0.0, -1.0))).unit_vector()
    c1 = vec3((N.x()+1, N.y()+1, N.z()+1)) * 0.5
    # skybox (default)
    unit_direction = r.direction.unit_vector()
    t2 = 0.5 * (unit_direction.y() + 1.0)
    c2 = vec3((1.0, 1.0, 1.0))*(1.0-t2) + vec3((0.5, 0.7, 1.0))*t2
    # choose return color
    return np.where(t > 0.0, c1, c2)

if __name__ == '__main__':
    # (y, x, colors)
    height = 1000
    width = 2000
    out_shape = (height, width, 3)

    # camera parameters
    lower_left_corner = vec3((-2.0, -1.0, -1.0))
    horizontal = vec3((4.0, 0.0, 0.0))
    vertical = vec3((0.0, 2.0, 0.0))
    origin = vec3((0.0, 0.0, 0.0))

    # begin timing
    t0 = time.time()

    # set up rays
    x = np.tile(np.linspace(0, (out_shape[1]-1)/out_shape[1], out_shape[1]), out_shape[0])
    y = np.repeat(np.linspace(0, (out_shape[0]-1)/out_shape[0], out_shape[0]), out_shape[1])
    r = ray(origin = origin, direction = lower_left_corner + horizontal * x + vertical * y)

    # compute colors
    color = skybox_color(r)

    # rearrange results into correct image
    data = color.reshape((3,height,width))
    data = np.swapaxes(data, 0, 2)
    data = np.swapaxes(data, 0, 1)
    data = np.flip(data, 0)

    # stop timing
    print("Took", time.time() - t0, "s")

    # save to file
    matplotlib.image.imsave('out.png', data)

