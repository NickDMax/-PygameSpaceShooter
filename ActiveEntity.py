from Entity import Entity
import math

class ActiveEnity(Entity):
    def __init__(self, x: float = 0, y: float = 0, speed: float = 0, angle: float = math.pi / 2, file: str = None):
        super().__init__(x=x, y=y, speed=speed, angle=angle, file=file)
    


