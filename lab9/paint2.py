import pygame
pygame.init()

#screen settings
screen = pygame.display.set_mode([1200,600])
clock = pygame.time.Clock()
screen.fill(pygame.Color('white')) 

draw = False                # click - draw
radius = 10                 # radius for tools
color = 'blue'              # base color
mode = 'line'               # basic mode

def drawCircle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    #the formula for the center of the circle
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)

def drawRectangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    # draw the lines that make up the rectangle
    pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x2,y1),width)
    pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x1,y2),width)
    pygame.draw.line(screen,pygame.Color(color),(x1,y2),(x2,y2),width)
    pygame.draw.line(screen,pygame.Color(color),(x2,y1),(x2,y2),width)

def drawSquare(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    # draw the lines that make up the square, the length of which is the minimum change in the position of x or y
    if dx>dy:
        if x1 > x2:
            x2 = x1-dy
        else:
            x2 = x1+dy
    else:
        if y1 > y2:
            y2 = y1 - dx
        else:
            y2 = y1 + dx
    pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x2,y1),width)
    pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x1,y2),width)
    pygame.draw.line(screen,pygame.Color(color),(x1,y2),(x2,y2),width)
    pygame.draw.line(screen,pygame.Color(color),(x2,y1),(x2,y2),width)

def draw_Right_triangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    if y1 < y2:
        pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x2,y2),width)
        pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x1,y2),width)
        pygame.draw.line(screen,pygame.Color(color),(x1,y2),(x2,y2),width)
    else:
        pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x2,y2),width)
        pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x2,y1),width)
        pygame.draw.line(screen,pygame.Color(color),(x2,y2),(x2,y1),width)
    
def draw_Equilateral_triangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    dx = abs(x2-x1)
    if y1 < y2:
        pygame.draw.line(screen,pygame.Color(color),((x1+x2)/2,y2 - 3**0.5*dx/2),(x1,y2),width)
        pygame.draw.line(screen,pygame.Color(color),((x1+x2)/2,y2 - 3**0.5*dx/2),(x2,y2),width)
        pygame.draw.line(screen,pygame.Color(color),(x1,y2),(x2,y2),width)
    else:
        pygame.draw.line(screen,pygame.Color(color),((x1+x2)/2,y1 - 3**0.5*dx/2),(x1,y1),width)
        pygame.draw.line(screen,pygame.Color(color),((x1+x2)/2,y1 - 3**0.5*dx/2),(x2,y1),width)
        pygame.draw.line(screen,pygame.Color(color),(x1,y1),(x2,y1),width)
def drawRhombus(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    # draw the lines that make up the rectangle
    pygame.draw.line(screen,pygame.Color(color),((x1+x2)/2,y1),(x2,(y1+y2)/2),width)
    pygame.draw.line(screen,pygame.Color(color),(x2,(y1+y2)/2),((x1+x2)/2,y2),width)
    pygame.draw.line(screen,pygame.Color(color),((x1+x2)/2,y2),(x1,(y1+y2)/2),width)
    pygame.draw.line(screen,pygame.Color(color),(x1,(y1+y2)/2),((x1+x2)/2,y1),width)

prevX = 0
prevY = 0

while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        # pressing the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                mode = 'line'
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_a:
                mode = 'Rtriangle'
            if event.key == pygame.K_i:
                mode = 'Etriangle'
            if event.key == pygame.K_j:
                mode = 'Rhombus'
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_y:
                color = 'yellow'
            if event.key == pygame.K_b:
                color = 'blue'
            if event.key == pygame.K_g:
                color = 'green'
            if event.key == pygame.K_UP:
                radius = min(200, radius + 1)   
            if event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)     

        # clicking on the left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN: 
            draw = True
            prevX =  event.pos[0]
            prevY =  event.pos[1]
            prevPos = event.pos
        
        # the initial position of the mouse
        currentX = prevX
        currentY = prevY
        
        # release the left mouse button
        if event.type == pygame.MOUSEBUTTONUP: 
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, radius, color)
            elif mode == 'Rtriangle':  
                draw_Right_triangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'Etriangle':  
                draw_Equilateral_triangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'Rhombus':  
                drawRhombus(screen, prevPos, event.pos, radius, color)
            draw = False

        # moving the mouse
        if event.type == pygame.MOUSEMOTION: 
            if draw:
                if mode == 'line' or mode == 'erase':
                    # changing the position
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
            
        
        if mode == 'line' and draw == True:
            pygame.draw.circle(screen, color, (currentX, currentY), radius)
        if mode == 'erase' and draw == True:
            pygame.draw.circle(screen, (255,255,255), (currentX, currentY), radius)
        prevX = currentX
        prevY = currentY
    
    # display
    pygame.display.flip()
    clock.tick(60)