from pygame import image

class Background(object):
    def __init__(self, canvas_h, canvas_w):
        self._bk = []
        self._index = -1
        self._canvas_h = canvas_h
        self._canvas_w = canvas_w
        self._x = 0
        self._y = 0
        self.rel_x = 0
        self.rel_y = 0
        self.speed_x = 0
        self.speed_y = 1

    
    def load(self, file, atindex = None):
        if atindex is None or atindex >= len(self._bk):
            self._bk.append(image.load(file))
        else:
            if atindex < len(self._bk):
                self._bk.insert(image.load(file))
        self.index = self.index
        
    def __len__(self):
        return len(self._bk)
    
    @property 
    def index(self):
        return self._index
    
    @index.setter
    def index(self, value):
        self._index = value % len(self)
    
   
    @property
    def current(self):
        return self._bk[self._index]
    
    @property
    def next(self):
        return self._bk[(self._index + 1) % len(self)]        
 
    @property
    def last(self):
        return self._bk[(self._index - 1) % len(self)]

    @property
    def height(self):
        return self.current.get_rect().height
    
    @property
    def width(self):
        return self.current.get_rect().width
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x
        if self._x < 0:
            self._x = 0
        if self._x + self.width > self._canvas_w:
            self._x = self._canvas_w - self.width

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y

    
    def update(self, dx = None, dy = None):
        if dx is not None:
            self.x += dx
        else:
            self.x += self.speed_x
 
                
        
        if dy is not None:
            self.y += dy
        else:
            self.y += self.speed_y
        
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
        
        