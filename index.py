import pygame
import random

pygame.init()

ancho = 640
alto = 480
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game")

blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
negro = (0, 0, 0)

posicion_snake = [100, 50]
cuerpo_snake = [[100, 50]]
direccion = "RIGHT"
cambio_direccion = direccion
tamano_serpiente = 1
tamano_maximo = 20
comida_pos = [random.randrange(0, ancho // 10)
              * 10, random.randrange(0, alto // 10) * 10]

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                cambio_direccion = "UP"
            if evento.key == pygame.K_DOWN:
                cambio_direccion = "DOWN"
            if evento.key == pygame.K_LEFT:
                cambio_direccion = "LEFT"
            if evento.key == pygame.K_RIGHT:
                cambio_direccion = "RIGHT"

    if cambio_direccion == "UP" and not direccion == "DOWN":
        direccion = "UP"
    if cambio_direccion == "DOWN" and not direccion == "UP":
        direccion = "DOWN"
    if cambio_direccion == "LEFT" and not direccion == "RIGHT":
        direccion = "LEFT"
    if cambio_direccion == "RIGHT" and not direccion == "LEFT":
        direccion = "RIGHT"

    if direccion == "UP":
        posicion_snake[1] -= 10
    if direccion == "DOWN":
        posicion_snake[1] += 10
    if direccion == "LEFT":
        posicion_snake[0] -= 10
    if direccion == "RIGHT":
        posicion_snake[0] += 10

    if posicion_snake[0] >= ancho or posicion_snake[0] < 0 or posicion_snake[1] >= alto or posicion_snake[1] < 0:
        pygame.quit()
        quit()

    for segmento in cuerpo_snake[1:]:
        if posicion_snake == segmento:
            pygame.quit()
            quit()

    if posicion_snake == comida_pos:
        tamano_serpiente += 1
        comida_pos = [random.randrange(
            0, ancho // 10) * 10, random.randrange(0, alto // 10) * 10]

    cuerpo_snake.insert(0, list(posicion_snake))

    if len(cuerpo_snake) > tamano_serpiente:
        cuerpo_snake.pop()

    pantalla.fill(negro)
    for segmento in cuerpo_snake:
        pygame.draw.rect(pantalla, blanco, pygame.Rect(
            segmento[0], segmento[1], 10, 10))
    pygame.draw.rect(pantalla, rojo, pygame.Rect(
        comida_pos[0], comida_pos[1], 10, 10))

    pygame.display.update()
    reloj.tick(15)
