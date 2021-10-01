import math
from pygame import Surface, Vector2, image, transform, math as pmath
from collections import namedtuple
Point = namedtuple("Point", ['x', 'y'])


class Entity(object):
    _sprite: list
    _index: int
    _x: float
    _y: float
    _vector: Vector2
    _rotation: float
    _tick: float
    _display: bool
    _animate: bool
    _delay_ticks: int
    _loop: bool
    _counter: int

    def __init__(self, x: float = 0, y: float = 0, speed: float = 0, angle: float = math.pi/2, file: str = None):
        self._sprite = []
        self._index = 0
        self._x = x
        self._y = y
        self._speed = speed
        self._angle = angle
        self._vector = pmath.Vector2(
            speed * math.cos(angle), speed * math.sin(angle))
        self._rotation = 0
        self._tick = 0
        self._display = True
        self._animate = False
        self._delay_ticks = 10
        self._loop = False

        if file is not None:
            self._sprite.append(image.load(file))

    def load(self, file) -> None:
        self._sprite.append(image.load(file))
        self.index = self.index
        self._loop = len(self)

    def loadGroup(self, fileList: list) -> None:
        for f in fileList:
            self.load(f)

    def __len__(self) -> int:
        return len(self._sprite)

    @property
    def display(self) -> bool:
        return self._display

    @display.setter
    def display(self, display):
        self._display = display

    @property
    def animate(self) -> bool:
        return self._animate

    @animate.setter
    def animate(self, animate):
        self._animate = animate
        self._counter = len(self) + 1

    @property
    def loop(self) -> bool:
        return self._loop

    @loop.setter
    def loop(self, loop):
        self._loop = loop
        self._counter = len(self) + 1

    @property
    def tick(self) -> float:
        return self._tick

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int):
        self._index = value % len(self)

    @property
    def current(self) -> Surface:
        return self._sprite[self._index]

    @property
    def next(self) -> Surface:
        return self._sprite[(self._index + 1) % len(self)]

    @property
    def last(self) -> Surface:
        return self._sprite[(self._index - 1) % len(self)]

    @property
    def height(self) -> int:
        return self.current.get_rect().height

    @property
    def width(self) -> int:
        return self.current.get_rect().width

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float):
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float):
        self._y = y

    @property
    def pos(self) -> Point:
        return Point(self._x, self._y)

    @pos.setter
    def pos(self, corrd: Point) -> None:
        (self._x, self._y) = corrd

    @property
    def center(self) -> Point:
        """The center property."""
        return Point(self.x + self.width // 2, self.y + self.height // 2)

    @center.setter
    def center(self, value: Point) -> None:
        self._x = value[0] - self.width // 2
        self._y = value[1] - self.height // 2

    def manhattanDistanceTo(self, other: 'Entity') -> Point:
        center = self.center
        centerO = other.center
        return Point(centerO.x - center.x, centerO.y - center.y)

    def distanceTo(self, other: 'Entity'):
        md = self.manhattanDistanceTo(other)
        math.sqrt(md.x ** 2 + md.y ** 2)

    @property
    def vector(self) -> Vector2:
        return self._vector

    @vector.setter
    def vector(self, vec: Vector2) -> None:
        self._vector = vec

    @property
    def speed(self) -> float:
        return self._vector.magnitude()

    @speed.setter
    def speed(self, value: float) -> None:
        self.vector.from_polar((value, self.angle*(180/math.pi)))

    @property
    def angle(self) -> float:
        (_, phi) = self.vector.as_polar()
        return phi * math.pi/180

    @angle.setter
    def angle(self, value) -> None:
        self.vector.from_polar((self._vector.magnitude(), value*(180/math.pi)))
        # self._setdxdy()

    def targetOther(self, other: 'Entity') -> None:
        md = self.manhattanDistanceTo(other)
        self.angle = math.atan2(md.y, md.x)

    def target(self, x: float, y: float):
        center = self.center
        self.angle = math.atan2(y-center.y, x - center.x)

    def update(self, dx: float = None, dy: float = None) -> None:
        self._tick += 1
        if self._animate and self._tick % self._delay_ticks == 0:
            self.index += 1
            if self.index == 0:
                if not self.loop:
                    self._animate = False
                    self._display = False
                    return
        if dx:
            self._x += dx
        else:
            self._x += self._vector[0]
            
        if dy:
            self._y += dy
        else:
            self._y += self._vector[1]

    def draw(self, canvas: Surface) -> None:
        if self._display:
            canvas.blit(self.current, self.pos)
