# AirBattle/game.py
import pygame
from pygame.locals import *
from utils import load_sprite, JoystickHandler, Object


class AirBattle:
    def __init__(self):
        # initialize pygame and set the title
        pygame.init()
        pygame.event.set_blocked((MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN))
        pygame.display.set_caption("Air Battle")
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        self.joy_count = pygame.joystick.get_count()
        if self.joy_count == 0:
            print("No controller detected!")
            quit()
        self.joy = []
        for i in range(self.joy_count):
            self.joy.append(JoystickHandler(i))

        self.screen = pygame.display.set_mode((1280, 720))
        self.background = load_sprite("decor", False)

        self.obj = Object("avion_D", True)
        self.obj.angle = 0
        self.obj.rect = (100, 100)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.obj)

    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == JOYAXISMOTION:
                self.joy[event.joy].axis[event.axis] = event.value
            elif event.type == JOYBUTTONUP:
                self.joy[event.joy].button[event.button] = 0
            elif event.type == JOYBUTTONDOWN:
                self.joy[event.joy].button[event.button] = 1

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        for sprite in self.all_sprites:
            sprite.move(self.joy[0].axis[1])
            self.screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()
        self.clock.tick(30)  # limite a 30 FPS
