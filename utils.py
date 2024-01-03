# AirBattle/utils.py
from pygame.image import load
from pygame.joystick import Joystick
from pygame.sprite import Sprite
from pygame.transform import rotate
from pathlib import Path
from math import cos, sin, pi


def load_sprite(name, with_alpha=True):
    filename = Path(__file__).parent / Path("assets/sprites/" + name + ".png")
    sprite = load(filename.resolve())
    
    if with_alpha:
        return sprite.convert_alpha()
        
    return sprite.convert()


class JoystickHandler(object):
    def __init__(self, num_id):
        self.id = num_id
        self.joy = Joystick(num_id)
        self.name = self.joy.get_name()
        self.joy.init()
        self.num_axes = self.joy.get_numaxes()
        self.num_buttons = self.joy.get_numbuttons()

        self.axis = []
        for i in range(self.num_axes):
            self.axis.append(self.joy.get_axis(i))

        self.button = []
        for i in range(self.num_buttons):
            self.button.append(self.joy.get_button(i))


class Object(Sprite):
    def __init__(self, name):
        super(Object, self).__init__()
        self.og_surf = load_sprite(name)
        self.surf = self.og_surf
        self.rect = self.surf.get_rect(center=(400, 400))
        self.speed = 5
        self.angle = 0
        self.change_angle = 0

    def rot(self):
        self.surf = rotate(self.og_surf, self.angle)
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)

    def move(self, norm_angle):
        self.change_angle = int(norm_angle * 3.0)
        self.rot()
        self.rect.x += cos(float(self.angle)*pi/180.0) * self.speed
        self.rect.y -= sin(float(self.angle)*pi/180.0) * self.speed
