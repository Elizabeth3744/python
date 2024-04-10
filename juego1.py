import pygame
pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("DVD :)")
ball = pygame.image.load("pelota3.webp")
ancho_deseado = 100
alto_deseado = 100
ball = pygame.transform.scale(ball, (ancho_deseado, alto_deseado))
ballrect = ball.get_rect()
speed = [10,10]


ballrect.move_ip(0,0)
# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("barra2.webp")
ancho_desead = 200
alto_desead = 100
bate = pygame.transform.scale(bate, (ancho_desead, alto_desead))
baterect = bate.get_rect()
# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240, 450)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3,0)
    if keys[pygame.K_UP]:
        baterect = baterect.move(0, -3)
    if keys[pygame.K_DOWN]:
        baterect = baterect.move(0, 3)
    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
 
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    if ballrect.bottom > ventana.get_height():
        pygame.quit()
    ventana.fill((252, 243, 207))
    ventana.blit(ball, ballrect)
    # Dibujo el bate
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
#la clase es el plano
