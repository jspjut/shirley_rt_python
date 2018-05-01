# simple vec3 class
import numpy as np

class vec3:
    def __init__(self, data = np.array((0.0, 0.0, 0.0))):
        '''store data as a np.array()'''
        self.data = np.array(data)
    def x(self): return self.data[0]
    def y(self): return self.data[1]
    def z(self): return self.data[2]
    def r(self): return self.data[0]
    def g(self): return self.data[1]
    def b(self): return self.data[2]
    def __add__(self, other):
        return vec3(data=(self.x() + other.x(), self.y() + other.y(), self.z() + other.z()))
    def __sub__(self, other):
        return vec3(data=(self.x() - other.x(), self.y() - other.y(), self.z() - other.z()))
    def __truediv__(self, scalar):
        '''divide by scalar'''
        return vec3(data=(self.x() / scalar, self.y() / scalar, self.z() / scalar))
    def __mul__(self, scalar):
        '''multiply by scalar'''
        return vec3(data=(self.x() * scalar, self.y() * scalar, self.z() * scalar))
    def __getitem__(self, index):
        return self.data[index]
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return 'vec3:' + str(self.data)
    def length(self):
        return np.sqrt(self.x()**2 + self.y()**2 + self.z()**2)
    def squared_length(self):
        return self.x()**2 + self.y()**2 + self.z()**2
    def unit_vector(self):
        return self / self.length()
    def dot(self, other):
        '''dot product of two vectors'''
        return self.x() * other.x() + self.y() * other.y() + self.z() * other.z()
    def cross(self, other):
        '''cross product of two vectors'''
        return vec3(data=(
            self[1] * other[2] - self[2] * other[1],
            -(self[0] * other[2] - self[2] * other[1]),
            self[0] * other[1] - self[1] * other[0]
        ))

