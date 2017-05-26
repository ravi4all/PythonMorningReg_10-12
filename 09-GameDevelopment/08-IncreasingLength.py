# Import pygame module
import pygame
import random

# Initialize pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = 0,0,0

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
FPS = 10

def snakeLength(snake):
    snake_tail = pygame.draw.rect(screen,black,[20,20,20,20])
    snake.append(snake_tail)

def mainLoop():

    x = 0
    y = 0

    x_width = 20

    snake = []

    move_x = 0
    move_y = 0

    enemy_x = random.randint(0,width-20)
    enemy_y = random.randint(0,height-20)

    while True:

        # Event Handling
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = +20
                    move_y = 0
                if event.key == pygame.K_LEFT:
                    move_x = -20
                    move_y = 0
                if event.key == pygame.K_UP:
                    move_y = -20
                    move_x = 0
                if event.key == pygame.K_DOWN:
                    move_y = +20
                    move_x = 0

        screen.fill(white)

        rect_1 = pygame.draw.rect(screen, red,[x,y,20,20])
        rect_2 = pygame.draw.rect(screen, black,[enemy_x, enemy_y, 20, 20])

        rect_3 = pygame.Rect(x+20,y+20,20,20)
        
        x += move_x
        y += move_y

        snake.append(rect_1)

        pygame.display.update()

        if rect_1.colliderect(rect_2):
            enemy_x = random.randint(0,width)
            enemy_y = random.randint(0,height)
            #x_width += 20
            snakeLength(snake)
            #print("Collision Detection")
        
        clock.tick(FPS)

mainLoop()
