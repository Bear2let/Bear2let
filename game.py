# AirBattle/game.py
import pygame
from pygame.joystick import Joystick
from pygame.locals import *
from utils import load_sprite, Object


class AirBattle:
    def __init__(self):
        # initialize pygame and set the title
        pygame.init()
        pygame.event.set_blocked((MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN))
        pygame.display.set_caption("Air Battle")
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Are Joysticks connected ?
        if pygame.joystick.get_count() == 0:
            print("No controller detected!")
            quit()

        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.background = load_sprite("decor", False)

        self.player_1 = Object("avion_D", True)
        self.player_1.stick = Joystick(0)
        self.player_1.angle = 0
        self.player_1.rect.x = 100
        self.player_1.rect.y = 100
        self.players = pygame.sprite.Group()
        self.players.add(self.player_1)

        self.missiles = pygame.sprite.Group()

    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def _game_logic(self):
        for player in self.players:
            if player.stick.get_axis(4) > 0 and not player.missile_actif:
                self.missile_1 = Object("missile_D", False)
                self.missile_1.stick = player.stick
                self.missile_1.angle = player.angle
                self.missile_1.rect.x = player.rect.x
                self.missile_1.rect.y = player.rect.y
                player.missile_actif = True
                self.missiles.add(self.missile_1)

        # pygame.sprite.spritecollide() collision entre avion et groupe (missiles + balles)
        pass

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        for player in self.players:
            player.move(player.stick.get_axis(1))
            self.screen.blit(player.surf, player.rect)
        for missile in self.missiles:
            missile.move(missile.stick.get_axis(3))
            self.screen.blit(missile.surf, missile.rect)
        pygame.display.flip()
        self.clock.tick(30)  # limite a 30 FPS
