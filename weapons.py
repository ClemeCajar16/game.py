import pygame
import constantes


class Weapon():

    def __init__(self, image):
        self.image_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje):
        self.forma.center = personaje.forma.center
        self.forma.x += personaje.forma.width / 2


    def dibujar(self, interfaz):
        interfaz.blit(self.imagen, self.forma)
        # pygame.draw.rect(interfaz,constantes.COLOR_ARMA , self.forma, width=2)