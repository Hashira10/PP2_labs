import pygame
from math import sin, cos, pi
import datetime

size = 700
center = size / 2, size / 2

pygame.init()
screen = pygame.display.set_mode([size, size])
clock = pygame.time.Clock()

mickey = pygame.image.load('m.png')
Left = pygame.transform.scale(pygame.image.load('left.png'), (770 // 2, 230 // 2))
Right = pygame.transform.scale(pygame.image.load('right.png'), (594 // 2, 322 // 2))

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0]- originPos[0], pos[1] - originPos[1]))
    #смещение центра для поворота
    centerPivot = pygame.math.Vector2(pos) - image_rect.center
    RotateOfsett = centerPivot.rotate(angle)
    RotatedCenter = (pos[0] - RotateOfsett.x, pos[1] - RotateOfsett.y)
    RotatedImage = pygame.transform.rotate(image, -angle)
    RotatedImage_rect = RotatedImage.get_rect(center = RotatedCenter)
    surf.blit(RotatedImage, RotatedImage_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            exit()

    screen.fill(pygame.Color('white'))
    screen.blit(mickey, (size/2 - 1200/2, size/2 - 900/2))

    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute

    theta = (minute + second/60) * (360 / 60)
    blitRotate(screen, Right, center, (Right.get_width() / 2 + 110, Left.get_height() / 2 + 75), theta + 75)

    theta = second * (360 / 60)
    blitRotate(screen, Left, center, (Left.get_width() / 2 - 145, Left.get_height() / 2), theta - 87)

    pygame.display.flip()
    clock.tick(60)
