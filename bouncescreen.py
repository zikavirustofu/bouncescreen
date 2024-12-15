import pygame


pygame.init()
screenx, screeny = 1280, 720
screen = pygame.display.set_mode((screenx, screeny), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("bouncingthing")



rectx, recty = 128, 96
velx, vely = 8, 8
thing = pygame.Rect((640, 360), (rectx, recty))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # make whole screen black
    screen.fill("black")

    # the rendering
    pygame.draw.rect(screen, (255, 255, 255), thing)

    # the processing
    coord = thing.topleft
    if ((coord[0] + velx) > (screenx - rectx)) or ((coord[0] + velx) < 0):
        velx = -velx
    if (coord[1] + vely) > (screeny - recty) or ((coord[1] + vely) < 0):
        vely = -vely
    thing = thing.move(velx, vely)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24)  # limits FPS to 60

pygame.quit()