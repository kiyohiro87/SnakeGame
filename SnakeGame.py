import pygame
import random
import time

pygame.init()
pygame.display.set_caption('Snake game by kiyohiro')
display_width = 900
display_height  = 600
display = pygame.display.set_mode((display_width,display_height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
gray = (120, 120, 120)
blue = (50, 153, 213)
green = (0, 255, 0)
yellow = (255, 255, 102)

#each snake block size
snake_block = 15

snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def draw_borders():
    for i in range(int(display_width / snake_block)):
        pygame.draw.rect(display, gray, [snake_block * i, 0, snake_block, snake_block])
        pygame.draw.rect(display, gray, [snake_block * i, display_height - snake_block, snake_block, snake_block])

    for i in range(int(display_height / snake_block)):
        pygame.draw.rect(display, gray, [0, snake_block * i, snake_block, snake_block])
        pygame.draw.rect(display, gray, [display_width - snake_block, snake_block * i, snake_block, snake_block])

def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_width / 6, display_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    snake_list = []
    snake_length = 1

    # initial position
    x1 = display_width / 2
    y1 = display_height / 2

    # starts without movement 
    x1_change = 0
    y1_change = 0

    # food position
    foodx = round(random.randrange(0 + snake_block, display_width - (snake_block * 2)) / 15.0) * 15.0
    foody = round(random.randrange(0 + snake_block, display_height - (snake_block * 2)) / 15.0) * 15.0

    while not game_over:
        while game_close == True:
            display.fill(blue)
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
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        if (x1 >= (display_width - snake_block) or (x1 < 0 + snake_block) or (y1 >= display_height - snake_block) or (y1 < 0 + snake_block)):
            game_close = True

        display.fill(blue)

        # print the food
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])

        # print the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
 
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
 
        our_snake(snake_block, snake_list)

        draw_borders()

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0 + snake_block, display_width - (snake_block * 2)) / 15.0) * 15.0
            foody = round(random.randrange(0 + snake_block, display_height - (snake_block * 2)) / 15.0) * 15.0
            snake_length += 1

        # snake speed
        clock.tick(snake_speed)

    message("You lost", red)
    pygame.display.update()
    time.sleep(1)
    
    pygame.quit()
    quit()

gameLoop()