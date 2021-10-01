from pygame import image
from Entity import Entity

class Background(Entity):
    def __init__(self, canvas_h, canvas_w):
        super().__init__()
        self._canvas_h = canvas_h
        self._canvas_w = canvas_w
        self.rel_x = 0
        self.rel_y = 0
    
    def update(self, dx = None, dy = None):
        if dx is not None:
            self.x += dx
        else:
            self.x += self.vector[0]
        
        if dy is not None:
            self.y += dy
        else:
            self.y += self.vector[1]
        
        self.rel_x =  self.x % self.width
        self.rel_y =  self.y % self.height
        
        if self.rel_y == 0:
            self.index += 1
            
    def draw(self, canvas, x=None, y=None):
        if x is not None:
            self.rel_x = x % self._canvas_w
        if y is not None:
            self.rel_y = y % self._canvas_h
            
        canvas.blit(self.next, (self.rel_x, self.rel_y - self.height))
        if self.rel_y < self._canvas_h:
            canvas.blit(self.current, (self.rel_x, self.rel_y))
        if self.rel_y+self.height < self._canvas_h:
            canvas.blit(self.last, (self.rel_x, self.rel_y))
        
        