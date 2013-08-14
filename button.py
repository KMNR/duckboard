from helpers import load_image
import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, color, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(color + '.png')
        if rect is not None:
            self.rect = rect

