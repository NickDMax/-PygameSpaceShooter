import pygame
from Layer import Layer
from Entity import Entity
import random

class MeteorShower(Layer):

    def __init__(self, H:int, W:int, filelist: list, target: Entity):
        super().__init__()
        self.autoAdd(filelist)
        self.H = H
        self.W = W
        
        for _, e in self.entities.items():
            e.speed = 0.5 + 2 * random.random()
            e.x = int(W * random.random())
            e.y = -int(H * random.random())
            scatter_x = W // 4 - (W // 4) * random.random()
            scatter_y = H // 4 - (H // 4) * random.random()
            e.target(target.x + scatter_x, target.y +scatter_y )
    
    
    def retarget(self, target: Entity) -> None:
        for _, e in self.entities.items():
            if e.y > self.H:
                e.speed = 0.5 + 2 * random.random()
                e.x = int(self.W * random.random())
                e.y = -int(self.H * random.random())                
                e.targetOther(target)
                
    def intersects(self, taget: Entity):
        rects = [e.current.get_rect().move(e.pos) for _, e in self.entities.items()]
        crash = pygame.Rect.collidelist(taget.current.get_rect().move(taget.pos), rects)
        if (crash > 0):
            return rects[crash].clip(taget.current.get_rect().move(taget.pos))      