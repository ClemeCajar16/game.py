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
        if personaje.flip == False:
            self.forma.x += personaje.forma.width / 2
        if personaje.flip == True:
            self.forma.x -= personaje.forma.width / 2

    def rotar(self, rotar):
        if rotar == True: 
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=True, flip_y=False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

        else:
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=False, flip_y=False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):
        interfaz.blit(self.imagen, self.forma)
        # pygame.draw.rect(interfaz,constantes.COLOR_ARMA , self.forma, width=2)

    