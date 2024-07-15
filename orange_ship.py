from ursina import *
from random import randint

def update():
    global invaders, score, text

    
    player.x += (mouse.x - player.x) * 0.1  

    for invader in invaders:
        invader.y += time.dt * invader.dy 
        if invader.y < -.55:
            Entity(model="quad", scale=60, color=color.gray)
            player.y = 10
            Text(text="Game Over   Play Again?", origin=(0, 0), scale=2, color=color.red, background=True)

    for bullet in bullets:
        bullet.y += time.dt * bullet.dy
        hit_info = bullet.intersects()
        if hit_info.hit:
            bullet.x = 10
            if hit_info.entity in invaders:
                Audio("fire.wav")
                hit_info.entity.x = randint(-50, 50) * .01
                hit_info.entity.y = randint(80, 120) * .01 
                score += 1
                text.y = 10 
                text = Text(text=f"Score: {score}", position=(-.65, .4), origin=(0, 0), scale=2, color=color.red, background=True)


def input(key):
    global bullets
    if key == "left mouse down":
        Audio("Canon.wav")
        bullet = Bullet()
        bullets.append(bullet)


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = "circle"
        self.color = color.green
        self.scale = (.1, .2, .2)
        self.position = (0, -.5, -.1) 
        self.dx = .5


class Invader(Entity):
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = "quad"
        self.texture = "ace_black_ship.png"
        self.scale = .1 
        self.position = (randint(-50, 50) * .01, randint(80, 120) * .01, -.1)
        self.collider = "box" 
        self.dy = -.15


class Bullet(Entity):
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = "circle"
        self.color = color.red
        self.texture = "missile_two.png"
        self.scale = (.02, .1, .1)
        self.position = player.position
        self.y = player.y + .2
        self.collider = "box" 
        self.dy = .8


app = Ursina()

field_size = 19

Entity(model="quad", scale=60, texture="blue-skies.png")
field = Entity(model="quad", color=color.rgba(255, 255, 255, 0), scale=(12, 18), position=(field_size // 2, field_size // 2, -.01))

bullets = []
player = Player()
invaders = [] 

score = 0 
text = Text(text="")

for i in range(7):
    invader = Invader()
    invaders.append(invader)

camera.position = (field_size // 2, -18, -18)
camera.rotation_x = -56

app.run()
