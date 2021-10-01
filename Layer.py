from Entity import Entity
from pygame import Surface, image

class Layer(object):
    entities : dict[str, Entity]
    
    def __init__(self) -> None:
        self.entities = {}
        pass
    
    def __delitem__(self, key) -> None:
        self.entities.pop(key, None)
    
    def __getitem__(self, key) -> Entity:
        return self.entities[key]
    
    def __setitem__(self, key, value) -> None:
        self.entities[key] = value

    def add(self, name: str, ent: Entity) -> None:
       self.entities[name] = ent
    
    def autoAdd(self, filelist: list) -> None:
        for i,f in enumerate(filelist):
            self.add(str(i), Entity(file=f))
    
    def update(self) -> None:
        for _, e in self.entities.items():
            e.update()
    
    def draw(self, canvas) -> None:
         for _, e in self.entities.items():
            e.draw(canvas)
            