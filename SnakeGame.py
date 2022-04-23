import pygame
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

game_over = False

# initial position
x = display_width / 2
y = display_height / 2

snake_block = 15

# starts without movement 
x_change = 0       
y_change = 0

snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def draw_borders():
    for i in range(int(display_width / snake_block)):
        pygame.draw.rect(display, gray, [snake_block * i, 0, snake_block, snake_block])
        pygame.draw.rect(display, gray, [snake_block * i, display_height - snake_block, snake_block, snake_block])

    for i in range(int(display_height / snake_block)):
        pygame.draw.rect(display, gray, [0, snake_block * i, snake_block, snake_block])
        pygame.draw.rect(display, gray, [display_width - snake_block, snake_block * i, snake_block, snake_block])


def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_width / 2, display_height / 2])

while not game_over:
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
        game_over = True

    pygame.draw.rect(display, black, [x, y, snake_block, snake_block])

    draw_borders()

    pygame.display.update()

    # snake speed
    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(1)
 
pygame.quit()
quit()