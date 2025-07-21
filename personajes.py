import pygame
import constantes


class Personaje(): 
    def __init__(self, x, y, img):

        self.flip = False
        self.image = img

        self.forma = pygame.Rect(0, 0,constantes.ANCHO_JUGADOR , constantes.ALTO_JUGADOR ) 
        self.forma.center = (x, y)

    def dibujar(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, flip_y=False )
        interfaz.blit(image_flip, self.forma)
       #pygame.draw.rect(interfaz, constantes.COLOR_JUGADOR, self.forma)

    
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False

        self.forma.x += delta_x
        self.forma.y += delta_y

