import pygame
import constantes
from personajes import Personaje
from weapons import Weapon



pygame.init() 

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))

pygame.display.set_caption("zombie.py")

def escala_img(img, escale):
    w = img.get_width() 
    h = img.get_height()
    new_img = pygame.transform.scale(img, (w * escale, h * escale))
    return new_img


# ? ANIMACION DE PERSONAJE 
animation = []

for i in range(1, 5):
    img = pygame.image.load(f"assets//img//character//player//{i}.png")
    img = escala_img(img, constantes.SCALA_JUGADOR)
    animation.append(img)


jugador = Personaje(100, 100, animation)


# ? ANIMACION DE PISTOLA

imagen_pistola = pygame.image.load(f"assets//img//weapons//1.png").convert_alpha()
imagen_pistola = escala_img(imagen_pistola, constantes.SCALA_ARMA)

pistola = Weapon(imagen_pistola)




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

   
    # ? MOVIMIENTO DEL JUGADOR
    jugador.movimiento(delta_x=delta_x, delta_y=delta_y)


    # ? ACTUALIZAR JUGADOR
    jugador.update()


# ? ACTUALIZAR PISTOLA
    pistola.update(jugador)


# ? DIBUJAR JUGADOR
    jugador.dibujar(ventana)

    # ? DIBUJAR PISTOLA
    pistola.dibujar(ventana)


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