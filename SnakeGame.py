import pygame
import random
import time

pygame.init()
display_width = 900
display_height  = 600
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake game by kiyohiro')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
gray = (120, 120, 120)
blue = (0, 0, 255)

snake_block = 15
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)

def draw_borders():
    for i in range(int(display_width / snake_block)):
        pygame.draw.rect(display, gray, [snake_block * i, 0, snake_block, snake_block])
        pygame.draw.rect(display, gray, [snake_block * i, display_height - snake_block, snake_block, snake_block])

    for i in range(int(display_height / snake_block)):
        pygame.draw.rect(display, gray, [0, snake_block * i, snake_block, snake_block])
        pygame.draw.rect(display, gray, [display_width - snake_block, snake_block * i, snake_block, snake_block])


def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_width / 3, display_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    # initial position
    x = display_width / 2
    y = display_height / 2

    # starts without movement 
    x_change = 0
    y_change = 0

    foodx = round(random.randrange(0, display_width - snake_block) / 15.0) * 15.0
    foody = round(random.randrange(0, display_height - snake_block) / 15.0) * 15.0

    while not game_over:
        while game_close == True:
            display.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        x += x_change
        y += y_change
        display.fill(white)

        if (x >= (display_width - snake_block) or (x < 0 + snake_block) or (y >= display_height - snake_block) or (y < 0 + snake_block)):
            game_close = True

        # print the food
        pygame.draw.rect(display, blue, [foodx, foody, snake_block, snake_block])

        # print the snake
        pygame.draw.rect(display, black, [x, y, snake_block, snake_block])

        draw_borders()

        pygame.display.update()

        if x == foodx and y == foody:
            print("Yummy!")

        # snake speed
        clock.tick(snake_speed)

    message("You lost", red)
    pygame.display.update()
    time.sleep(1)
    
    pygame.quit()
    quit()

gameLoop()