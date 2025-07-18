import pygame
import constantes
from personajes import Personaje

jugador = Personaje(x=50, y=50)

pygame.init() 

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))

pygame.display.set_caption("zombie.py")

run = True
while run: 

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == 	pygame.K_LEFT: 
                print("izqierda")

            elif event.key == pygame.K_RIGHT: 
                print("derecha")

            elif event.key == 	pygame.K_UP:
                print("arriba")
            
            elif event.key == 	pygame.K_DOWN:
                print("abajo")

    pygame.display.update()

pygame.quit()