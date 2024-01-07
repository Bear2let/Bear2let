# AirBattle/utils.py
from pygame.image import load
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


class Object(Sprite):
    def __init__(self, name, avion=True):
        super(Object, self).__init__()
        self.og_surf = load_sprite(name)
        self.surf = self.og_surf
        self.rect = self.surf.get_rect(center=(400, 400))
        if avion:
            self.speed = 5
            self.rot_speed = 3
        else:
            self.speed = 10
            self.rot_speed = 6
        self.angle = 0
        self.change_angle = 0
        self.stick = None
        self.missile_actif = False

    def rot(self):
        self.surf = rotate(self.og_surf, self.angle)
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)

    def move(self, norm_angle):
        self.change_angle = int(norm_angle * self.rot_speed)
        self.rot()
        self.rect.x += cos(float(self.angle)*pi/180.0) * self.speed
        self.rect.y -= sin(float(self.angle)*pi/180.0) * self.speed
