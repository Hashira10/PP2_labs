import pygame

size = 500
step = 20
radius = 25
pygame.init()
screen = pygame.display.set_mode([size,size])
x,y = size/2,size/2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y >= radius*2:
                    y -= step
            if event.key == pygame.K_DOWN:
                if y <= size - radius*2:
                    y += step
            if event.key == pygame.K_RIGHT:
                if x <= size - radius*2:
                    x += step
            if event.key == pygame.K_LEFT:
                if x >= radius*2:
                    x -= step
    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen,(255,0,0),(x,y),radius)
    pygame.display.flip()
    clock.tick(60)