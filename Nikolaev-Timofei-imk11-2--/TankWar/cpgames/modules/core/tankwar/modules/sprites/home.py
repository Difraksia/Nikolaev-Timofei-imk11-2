import pygame


class Home(pygame.sprite.Sprite):
    def __init__(self, position, images, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.alive = True

    def setDead(self):
        self.image = self.images[1]
        self.alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)