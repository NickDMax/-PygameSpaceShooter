from collections import namedtuple
Point = namedtuple("Point", ['x','y'])

class GameState(object):
    
    def __init__(self) -> None:
        self._canvas_w = 640
        self._canvas_h = 480
        self._player_pos = Point(300, 400)
        self._player_canvas_pos = Point(300, 400)
        self._player_dax = 0
        self._player_ddx = 0
        self._player_dwy = 0
        self._player_dsy = 0        
        pass
    
    @property
    def player_pos(self):
        #print("getter method called")
        return self._player_pos
       
    # a setter function
    @player_pos.setter
    def player_pos(self, pos: Point):
        if(pos.x < 0):
           pos = Point(0, pos.y)
        if pos.y < 0:
            pos = Point(pos.x, 0)
        if(pos.x > self._canvas_w):
           pos = Point(self._canvas_w,pos.y)
        if pos.y > self._canvas_h:
            pos = Point(pos.x, self._canvas_h)           
        #print("setter method called")
        self._player_pos = pos
        
    def update_player_pos(self):
        self.player_pos = Point(
            self._player_pos.x + self._player_dax + self._player_ddx,  
            self._player_pos.y + self._player_dwy + self._player_dsy)
    
    @property
    def player_left(self):
        return self._player_dax
    
    @player_left.setter
    def player_left(self, d):
        self._player_dax = -abs(d)
         
    @property
    def player_right(self):
        return self._player_ddx
    
    @player_right.setter
    def player_right(self, d):
        self._player_ddx = abs(d)
    
    @property
    def player_up(self):
        return self._player_dwy
    
    @player_up.setter  
    def player_up(self, d):
        self._player_dwy = -abs(d)
    
    @property
    def player_down(self):
        return self._player_dsy
    
    @player_down.setter     
    def player_down(self, d):
        self._player_dsy = abs(d)
        
    def player_stop(self):
        self.player_left(0)
        self.player_right(0)
        self.player_down(0)
        self.player_up(0)

# game = GameState()

# game.player_pos = Point(-1,-1)
# print(game.player_pos)
# game.player_pos = Point(-1,1000)
# print(game.player_pos)
# game.player_pos = Point(1000, -1)
# print(game.player_pos)
# game.player_pos = Point(1000,1000)
# print(game.player_pos)
# game.update_player_pos()
# print(game.player_pos)
# game.player_left(5)
# game.update_player_pos()
# print(game.player_pos)
# game.update_player_pos()
# print(game.player_pos)
# game.player_left(0)
# game.update_player_pos()
# print(game.player_pos)
