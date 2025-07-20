import pygame
import constantes


class Personaje(): 
    def __init__(self, x,img):

        self.image = img

        self.forma = pygame.Rect(0, 0,constantes.ANCHO_JUGADOR , constantes.ALTO_JUGADOR ) 
        self.forma.center = (x, y)

    def dibujar(self, interfaz):
        interfaz.blit(self.image, self.forma)
        pygame.draw.rect(interfaz, constantes.COLOR_JUGADOR, self.forma)

    
    def movimiento(self, delta_x, delta_y):
        self.forma.x += delta_x
        self.forma.y += delta_y

