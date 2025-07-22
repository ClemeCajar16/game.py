import pygame

class Weapon():

    def __init__(self, image):
        self.image_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje):
        self.forma.center = personaje.forma.center