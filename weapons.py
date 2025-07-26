import pygame
import constantes
import math


class Weapon():

    def __init__(self, image, imagen_bala):
        
        self.image_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.imagen_bala = imagen_bala
        self.dispra = False

        # TODO: MOVER ARMA
    def update(self, personaje):

        bala = None

        self.forma.center = personaje.forma.center
        if personaje.flip == False:
            self.forma.x += personaje.forma.width / 2
            self.rotar(False)

        if personaje.flip == True:
            self.forma.x -= personaje.forma.width / 2
            self.rotar(True)

        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = - (mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))


        # ? CLIK DEL MAUSE
        if pygame.mouse.get_pressed()[0] and self.dispra == False:
            bala = Bullet(self.imagen_bala,self.forma.centerx, self.forma.centery, self.angulo)
            self.dispra = True
        
# ? RESETEAR CLICK MAUSE
        if not pygame.mouse.get_pressed()[0]:
            self.dispra = False
        return bala
        
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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        self.rect = self.image.get_rect(center=(x, y))


    def dibujar(self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx, self.rect.centery - (self.rect.height / 2)))