import pygame
import constantes

pygame.init() 

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))

pygame.display.set_caption("zombie.py")

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()