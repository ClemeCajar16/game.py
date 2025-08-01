import pygame
import constantes
from personajes import Personaje
from weapons import Weapon
import os



pygame.init() 

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))

pygame.display.set_caption("zombie.py")

def escala_img(img, escale):
    w = img.get_width() 
    h = img.get_height()
    new_img = pygame.transform.scale(img, (w * escale, h * escale))
    return new_img


# TODO: FUNCIONES

# ? CONTAR ELEMENTOS

def contar_elementos(directorio):

    return len(os.listdir(directorio))

print("Cantidad de elementos en el directorio:", contar_elementos("assets/img/character"))

#? LISTAR NOMBRE ELEMENTOS 

def nombres_carpetas(directorio):
    return os.listdir(directorio)

print(nombres_carpetas("assets/img/character/enemigos" ))

# ? ANIMACION DE PERSONAJE 
animation = []

for i in range(1, 5):
    img = pygame.image.load(f"assets//img//character//player//{i}.png")
    img = escala_img(img, constantes.SCALA_JUGADOR)
    animation.append(img)
     
    #? enemigos 
    directorio_enemigos = "assets/img/character/enemigos"
    tipos_enemigos = nombres_carpetas(directorio_enemigos)
    animacion_enemigos = []

    for enemy in tipos_enemigos:
        lista_temporal = []
        ruta_temporal = "assets/img/character/enemigos/" + enemy
        nume_animaciones = contar_elementos(ruta_temporal)
        
        for i in range (nume_animaciones): 
            img_enemigo = pygame.image.load(f"{ruta_temporal}/{enemy}_{i + 1}.png").convert_alpha()
            img_enemigo = escala_img(img_enemigo, constantes.ESCALA_ENEMIGOS)
            lista_temporal.append(img_enemigo)

        animacion_enemigos.append(lista_temporal)

        print(animacion_enemigos)




jugador = Personaje(100, 100, animation, energia=100)

# ? CREAR ENEMIGOS 
mounstruo = Personaje(x=400, y=300, animation=animacion_enemigos[0], energia=100)
zombie = Personaje(x=600, y=300, animation=animacion_enemigos[1], energia=100)
mounstruo2 = Personaje(x=450, y=350, animation=animacion_enemigos[0], energia=100)
zombie2 = Personaje(x=700, y=350, animation=animacion_enemigos[1], energia=100)


# LISTA DE ENEMIGOS
lista_enemigos = []
lista_enemigos.append(mounstruo)
lista_enemigos.append(zombie)
lista_enemigos.append(mounstruo2)
lista_enemigos.append(zombie2)

 

# ? BALAS
imagen_balas = pygame.image.load(f"assets//img//weapons//bala.png").convert_alpha()
imagen_balas = escala_img(imagen_balas, constantes.SCALA_BALA)

# ? ANIMACION DE PISTOLA

imagen_pistola = pygame.image.load(f"assets//img//weapons//1.png").convert_alpha()
imagen_pistola = escala_img(imagen_pistola, constantes.SCALA_ARMA)

pistola = Weapon(imagen_pistola, imagen_balas)

# ? GRUPO DE SPRITES
grupo_balas = pygame.sprite.Group()


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
    

    # ? ACTUALIZAR ENEMIGOS
    for enemigo in lista_enemigos:
        enemigo.update()
        
        print(enemigo.energia)



# ? ACTUALIZAR PISTOLA
    bala = pistola.update(jugador)
    if bala:
        grupo_balas.add(bala)

    for bala in grupo_balas:
        bala.update(lista_enemigos)

# ? DIBUJAR JUGADOR
    jugador.dibujar(ventana)

    # ? DIBUJAR ENEMIGOS
    for enemigo in lista_enemigos:
        enemigo.dibujar(ventana)

    # ? DIBUJAR PISTOLA
    pistola.dibujar(ventana)

    # ? DIBUJAR BALAS
    for bala in grupo_balas:
        bala.dibujar(ventana)

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