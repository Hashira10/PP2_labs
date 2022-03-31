import pygame
import datetime
from math import sin, cos, pi


size = 500
center = size / 2, size / 2
fps = 60

pygame.init()
screen = pygame.display.set_mode([size, size])
clock = pygame.time.Clock()
mickey = pygame.image.load('mickey.png')

leftHand = pygame.transform.scale(pygame.image.load('left.png'), (246 // 2, 165 // 2))
rightHand = pygame.transform.scale(pygame.image.load('right.png'), (196 // 2, 162 // 2))



def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            exit()
    screen.fill(pygame.Color('white'))
    screen.blit(mickey, (size/2 - 577/2, size/2 - 433/2))

    # time
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute

    # minute
    theta = (minute + second / 60) * (360 / 60)
    rot_center(rightHand, theta,196 // 2, 162 // 2 )

    # second
    theta = second * (360 / 60)
    rot_center(leftHand, theta,246 // 2, 165 // 2)


    # display
    pygame.display.flip()
    clock.tick(fps)