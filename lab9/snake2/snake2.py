import pygame
from random import randrange

width = 650
height = 650
block_size = 10
length = 1
score = 0
level = 0

wall = randrange(0, width, block_size), randrange(0, height, block_size)
x, y = randrange(0, width, block_size), randrange(0, height, block_size)
food1 = randrange(0, width, block_size), randrange(0, height, block_size)
food2 = randrange(0, width, block_size), randrange(0, height, block_size)
food3 = randrange(0, width, block_size), randrange(0, height, block_size)

snake = [(x, y)]
dx, dy = 0, 0
FPS = 10
d = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}

pygame.init()

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
score_settings = pygame.font.SysFont('Arial', 16, bold=True)
level_settings = pygame.font.SysFont('Arial', 16, bold=True)
end_settings = pygame.font.SysFont('Arial', 66, bold=True)
background = pygame.image.load('s_back.jpg').convert()

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == timer_event:
            food3 = randrange(0, width, block_size), randrange(0, height, block_size)   

    while food1 == wall or food1 == snake or food2 == wall or food2 == snake or food3 == wall or food3 == snake:
        food1 = randrange(0, width, block_size), randrange(0, height, block_size)
        food2 = randrange(0, width, block_size), randrange(0, height, block_size)
        food3 = randrange(0, width, block_size), randrange(0, height, block_size)

    screen.blit(background, (0, 0))

    # drawing snake and food
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('black'), (i, j, block_size - 1, block_size - 1))
    pygame.draw.rect(screen, pygame.Color('green'), (*wall, block_size, block_size ))
    pygame.draw.rect(screen, pygame.Color('yellow'), (*food2, block_size, block_size))
    pygame.draw.rect(screen, pygame.Color('orange'), (*food1, block_size, block_size))
    pygame.draw.rect(screen, pygame.Color('yellow'), (*food3, block_size, block_size))

    # score, level
    render_score = score_settings.render(f'SCORE: {score}', True, pygame.Color('red'))
    screen.blit(render_score, (5, 5))
    render_level = level_settings.render(f'LEVEL: {level}', True, pygame.Color('red'))
    screen.blit(render_level, (5, 20))   


    # movement
    x += dx * block_size
    y += dy * block_size
    snake.append((x, y))
    snake = snake[-length:]
        
    # eating food
    if snake[-1] == food1 or snake[-1] == food3:
        while food1 in snake:
            food1 = randrange(0, width, block_size), randrange(0, height, block_size)
        while food3 in snake:
            food3 = randrange(0, width, block_size), randrange(0, height, block_size)
        length += 1
        score += 1
        if score % 4 == 0 and score != 0:
            FPS += 2
            level += 1
        
    elif snake[-1] == food2:
        while food2 in snake:
            food2 = randrange(0, width, block_size), randrange(0, height, block_size)
        length += 2
        score += 2
        if score % 4 == 0 and score != 0:
            FPS += 2
            level += 1

    # motion control
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and d['UP']:
        d = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True} #If we go up we can't go down right away
        dx = 0
        dy = -1
        
    if key[pygame.K_DOWN] and d['DOWN']:
        d = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True} #If we go down we can't go up right away
        dx = 0
        dy = 1
        
    if key[pygame.K_RIGHT] and d['RIGHT']:
        d = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
        dx = 1
        dy = 0
        
    if key[pygame.K_LEFT] and d['LEFT']:
        d = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
        dx = -1
        dy = 0
        
    

    # game over if the snake goes over the wall or it collides with the length of its body
    if x < 0 or x > width - block_size or y < 0 or y > height - block_size or len(snake) > len(set(snake)) or snake[-1] == wall: 
        while True:
            render_end = end_settings.render('GAME OVER', True, pygame.Color('red'))
            screen.blit(render_end, (135, 280))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


    pygame.display.flip()
    clock.tick(FPS)