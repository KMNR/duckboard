#! /usr/bin/env python

import os
import sys
import pygame
from pygame.locals import *
airhorn = os.path.join('sounds', 'AirHorn-Reggae.wav')

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

import pygame.mixer
pygame.mixer.init(44100,-16,2,2048)
airhorn_sound = pygame.mixer.Sound(airhorn)

class DuckBoardController:
    """The Main DuckBoard Class - This class handles the main 
    initialization and creating of the GUI."""


    def __init__(self, width=640, height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((width, height))

 
    def run(self):
        """This is the Main Loop of the Controller"""
 
        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(500, 30)
 
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        default_color = 'green' 
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        default_color = 'red' if default_color == 'green' else 'green'
                        airhorn_sound.play()
                        print(event.key)
 
            """Draw the GUI text and boxes"""
            self.background.fill((0,0,0)) 
            rect = pygame.Rect(10, 10, 320, 24)
            pygame.draw.rect(self.background, pygame.Color(default_color), rect, 5)
            self.screen.blit(self.background, (0, 0)) 
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("DuckBoard Display", 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.background.get_width()/2)
                self.screen.blit(text, textpos)

            pygame.display.flip()


if __name__ == "__main__":
    controller = DuckBoardController()
    controller.run()
