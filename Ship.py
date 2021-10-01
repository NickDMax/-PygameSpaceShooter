import math
from Entity import Entity, Point

class Ship(Entity):
    """docstring for Ship."""
    def __init__(self, x = 0, y = 0, speed = 1, angle = math.pi/2, file = None):
        super(Ship, self).__init__(x,y,speed, angle, file)
        
        