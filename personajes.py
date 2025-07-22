import pygame
import constantes


class Personaje(): 
    def __init__(self, x, y, animation):

        self.flip = False
        self.animation = animation

        self.freme_index = 0
        self.image = self.animation[self.freme_index]
        self.update_time = pygame.time.get_ticks()

        self.forma = self.image.get_rect() 
        self.forma.center = (x, y)


    def update(self):
        cooldown_animation = 100
        self.image = self.animation[self.freme_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            self.freme_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.freme_index >= len(self.animation):
            self.freme_index = 0

    def dibujar(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, flip_y=False )
        interfaz.blit(image_flip, self.forma)
        # pygame.draw.rect(interfaz, constantes.COLOR_JUGADOR, self.forma, width=2)

    
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False

        self.forma.x += delta_x
        self.forma.y += delta_y

