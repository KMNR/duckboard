#! /usr/bin/env python

import os
import sys
import pygame
from pygame.locals import *
import settings
from profiles import default
import pygame.mixer
pygame.mixer.init(44100,-16,2,2048)

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

BACKGROUND_COLOR = (102, 51, 0)

class DuckBoardController:
    """The Main DuckBoard Class - This class handles the main 
    initialization and creating of the GUI."""


    def __init__(self, width=640, height=640):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((width, height))

        # Initialize all sound objects
        self.sounds = []
        for r in default.SOUNDS:
            sounds_for_row = []
            for filename in r:
                filepath = os.path.join('sounds', filename)
                sounds_for_row.append(pygame.mixer.Sound(filepath))

            self.sounds.append(sounds_for_row)
 
 
    def run(self):
        """This is the Main Loop of the Controller"""
 
        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(500, 30)
 
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(BACKGROUND_COLOR)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    try:
                        r, c = settings.ascii2coords[event.key]
                    except:
                        pass
                    else:
                        self.sounds[r][c].play()
                        print(unichr(event.key))
 
            """Draw the GUI text and boxes"""
            self.background.fill(BACKGROUND_COLOR)
            self.draw_button_areas()

            self.screen.blit(self.background, (0, 0)) 
            if pygame.font:
                font = pygame.font.Font(None, 16)
                text = font.render("DuckBoard Display", 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.background.get_width()/2)
                textpos.midleft = (20, 320)
                self.screen.blit(text, textpos)

            pygame.display.flip()

    def draw_button_areas(self):
      distance_between_boundaries = 10
      button_height = 32
      button_width = 305
      border_width = 1

      for row in xrange(0, 15):
        for col in xrange(0, 2):
          color = settings.COLORS[row][col]

          # If row == 0, then the top line should be at 10 pxs.
          #        == 1 -> 42
          #        == 2 -> 84
          #           ...
          top = distance_between_boundaries + row*(
                    button_height + distance_between_boundaries
                )

          # If col == 0, then the left line should be at 10 pxs.
          #        == 1 -> 10 + 305 + 10 = 325
          left = distance_between_boundaries + col*(
                    button_width + distance_between_boundaries
                 )

          rect = pygame.Rect(left, top, button_width, button_height)
          pygame.draw.rect(
              self.background, 
              pygame.Color(color), 
              rect,
              border_width
          )


if __name__ == "__main__":
    controller = DuckBoardController()
    controller.run()
