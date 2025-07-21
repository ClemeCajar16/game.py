import pygame
import constantes
from personajes import Personaje


pygame.init() 

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))

pygame.display.set_caption("zombie.py")

player = pygame.image.load("assets//img//character//player//01.png")
player = pygame.transform.scale(player, (player.get_width() * constantes.SCALA_JUGADOR, player.get_height() * constantes.SCALA_JUGADOR))
jugador = Personaje(x=50, y=50, img=player)

 

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False 

reloj = pygame.time.Clock()


run = True
while run: 
    
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = 4
    if mover_izquierda == True:
        delta_x = -4
    if mover_arriba == True:
        delta_y = -4    
    if mover_abajo == True:
        delta_y = 4

   

    jugador.movimiento(delta_x=delta_x, delta_y=delta_y)

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                mover_izquierda = True

            elif event.key == pygame.K_RIGHT: 
                mover_derecha = True

            elif event.key == 	pygame.K_UP:
                mover_arriba = True
            
            elif event.key == 	pygame.K_DOWN:
                mover_abajo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: 
                mover_izquierda = False

            elif event.key == pygame.K_RIGHT: 
                mover_derecha = False

            elif event.key == pygame.K_UP:
                mover_arriba = False
            
            elif event.key == pygame.K_DOWN:
                mover_abajo = False

    pygame.display.update()

pygame.quit()