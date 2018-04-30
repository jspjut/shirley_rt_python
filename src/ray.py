# simple ray class
##### TODO: fix src.vec3 import #####
from src.vec3 import vec3

class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    def point_at_parameter(self, t):
        return self.origin + self.direction * t
