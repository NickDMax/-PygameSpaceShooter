from ActiveEntity import ActiveEnity
from Entity import Entity
import time
import random
from pygame.math import Vector2
import pygame
from GameState import Point, GameState
from Background import Background
from MeteorShower import MeteorShower
from Layer import Layer
import math
import json


random.seed(time.time)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DIR_RIGHT = math.pi/2
DIR_UP = 0
DIR_LEFT = math.pi
DIR_DOWN = 0.75 * math.pi

VEC_RIGHT = Vector2(1, 0)
VEC_UP = Vector2(0, -1)
VEC_LEFT = Vector2(-1, 0)
VEC_DOWN = Vector2(0, 1)


def getGameData(datafile: str):
    try:
        f = open(datafile,)
        data = json.load(f)
    finally:
        f.close()
    return data


def handleEvents():
    for event in pygame.event.get():
        # print(pygame.event.event_name(event.type))
        if event.type == pygame.QUIT or \
            event.type == pygame.KEYDOWN and \
            ((event.key == pygame.K_q and event.mod & pygame.KMOD_ALT) or
             (event.key == pygame.K_ESCAPE)):

            print('!!QUIT!!')
            return False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            # if event.mod & pygame.KMOD_LCTRL:
            #    player.vector = player.vector + 2 * VEC_LEFT
            # else:
            player.vector = player.vector + 1 * VEC_LEFT
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            player.vector = player.vector - 1 * VEC_LEFT

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            # if event.mod & pygame.KMOD_LCTRL:
            #     player.vector = player.vector + 2 * VEC_RIGHT
            # else:
            player.vector = player.vector + 1 * VEC_RIGHT
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            player.vector = player.vector - 1 * VEC_RIGHT

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            # if event.mod & pygame.KMOD_LCTRL:
            #     player.vector = player.vector + 2 * VEC_UP
            # else:
            player.vector = player.vector + 1.25 * VEC_UP
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            player.vector = player.vector - 1.25 * VEC_UP
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            # if event.mod & pygame.KMOD_LCTRL:
            #     player.vector = player.vector + 2 * VEC_DOWN
            # else:
            player.vector = player.vector + 1.25 * VEC_DOWN
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            player.vector = player.vector - 1.25 * VEC_DOWN

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
            #player.speed = player.speed * 2
            # if game.player_down:
            #    game.player_down = 2
            # if game.player_up:
            #    game.player_up = 2
            # if game.player_left:
            #    game.player_left = 2
            # if game.player_right:
            #    game.player_right = 2
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
            #player.speed = player.speed/2
            # if game.player_down:
            #     game.player_down = 1.25
            # if game.player_up:
            #     game.player_up = 1.25
            # if game.player_left:
            #     game.player_left = 1
            # if game.player_right:
            #     game.player_right = 1
            pass

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass

    return True


game = GameState()

#os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d' % (-2560+200,100)
pygame.init()

fps = 120
CLOCK = pygame.time.Clock()
H = 480
W = 640
pygame.display.init()
canvas = pygame.display.set_mode([W, H])
pygame.display.set_caption('Space Shooter 1')

FONT = pygame.font.SysFont('Arial', 18)


def update_fps():
    fps = str(int(CLOCK.get_fps()))
    fps_text = FONT.render(fps, 1, pygame.Color('coral'))
    return fps_text


#bkgd = Layer()
bkgdLayer = Layer()

gamedata = getGameData('gamedata.json')
level = gamedata['level1']

bkgd = Background(H, W)
bkgd.loadGroup(level['backgrounds'])
bkgd.vector = VEC_DOWN

stars = Background(H, W)
stars.loadGroup(level['stars'])
stars.vector = VEC_DOWN

bkgdLayer['LevelSpace'] = bkgd
bkgdLayer['stars'] = stars


player = ActiveEnity()
player.loadGroup(gamedata['player']['ShipFly'])
player.animate = True
player.loop = True


ship_hw = player.width/2
canvas_hw = W/2
stars_hw = stars.width/2
stars_delta = canvas_hw - stars_hw
stars_x = stars_delta
ship_center = canvas_hw-ship_hw
player.pos = Point(ship_center, 400)
player.angle = DIR_UP

meteors = MeteorShower(H, W, filelist=level['meteorshower'], target=player)

boss = Entity()
boss.loadGroup(level['Enemies']['Boss'])
boss.center = Point(W/2, -H/4)
boss.speed = 0.25 + (random.random() * 0.25)
boss.target(player.pos.x, player.pos.y)

ship_hit = Entity()
ship_hit.loadGroup(gamedata['actions']['ShipHit'])
# ship_hit.load('resources/HUD/remove-score.png')
ship_hit.speed = 0
ship_hit.display = False
ship_hit.animate = True
ship_hit.loop = False

ship_explode = Entity()
ship_explode.loadGroup(gamedata['actions']['ShipExplode'])
ship_explode.display = False
ship_explode.animate = True
ship_explode.loop = False

healthbar = Entity()
healthbar.load('resources/HUD/HealthBar.png')
healthbar.load('resources/HUD/HealthBarColor.png')
healthbar.x = 30
healthbar.y = 5


hit = pygame.mixer.Sound('resources/Music/hit.wav')
pygame.mixer.music.load('resources/Music/1.ogg')
# pygame.mixer.music.play(-1,0.0)
point = 10
rest = False
# code.interact(local=locals()) # debugging tool....
while handleEvents():

    bkgdLayer['LevelSpace'].update()
    bkgdLayer['stars'].x = 0.25 * (canvas_hw-player.x+ship_hw) + stars_delta
    bkgdLayer['stars'].update(
        dy=1.25 + (-0.25 * game.player_up) + (0.25 * game.player_down))
    bkgdLayer.draw(canvas)

    meteors.update()
    meteors.draw(canvas)
    meteors.retarget(player)

    if boss.tick % 120 == 0:
        #ship.target(player.pos.x + ship_hw, player.pos.y)
        boss.targetOther(player)

    boss.update()
    boss.draw(canvas)

    canvas.blit(update_fps(), (5, 5))
    if not ship_explode.display:

        player.update()
        player.draw(canvas)
        player.index += 1
        ship_hit.update()
        ship_hit.draw(canvas)
        if not ship_hit.display:
            rest = False

        hitpoint = meteors.intersects(player)
        if hitpoint and not rest:
            hit.play()
            rest = True
            point -= 1
            ship_hit.display = True
            ship_hit.animate = True
            ship_hit.center = hitpoint.center
            if point == 0:
                ship_explode.display = True
                ship_explode.animate = True
                ship_explode.center = player.center
                point = 10
    else:
        ship_explode.update()
        ship_explode.draw(canvas)

    healthbar.update()
    canvas.blit(healthbar.current, healthbar.pos)
    hbrect = healthbar.next.get_rect()
    hbrect.width = hbrect.width * (1/10) * point
    #print(hbrect,  healthbar.next.get_rect())
    canvas.blit(healthbar.next.subsurface(hbrect),
                hbrect.move(healthbar.x+10, healthbar.y+6))

    pygame.display.flip()
    CLOCK.tick(fps)


pygame.mixer.music.stop()
pygame.display.quit()
