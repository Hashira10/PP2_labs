import pygame
import os

size = (720,450)
cnt = 0
w,a,s,d = False,False,False,False

pygame.init()
songs = []
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
muse = pygame.transform.scale(pygame.image.load('music.png'), size)

for i in os.listdir("C:\\Users\\Olga\\songs"):
    k = pygame.mixer.Sound("C:\\Users\\Olga\\songs\\" + str(i))
    songs.append(k)
songs[cnt].play()

while True:
    screen.fill(pygame.Color('white'))
    screen.blit(muse, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w = True
            if event.key == pygame.K_s:
                s = True
            if event.key == pygame.K_a:
                a = True
            if event.key == pygame.K_d:
                d = True
    if w == True:
        songs[cnt].play()
        w = False
    if s == True:
        if not pygame.mixer.pause():
            pygame.mixer.music.pause()
        s = False
    if a == True:
        songs[cnt].stop()
        cnt -= 1
        if cnt == -1:
            cnt = 6
        songs[cnt].play()
        a = False
    if d == True:
        songs[cnt].stop()
        cnt += 1
        if cnt == 7:
            cnt = 0
        songs[cnt].play()
        d = False

    pygame.display.flip()
