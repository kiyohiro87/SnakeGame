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

    if x >= display_width or x < 0 or y >= display_height or y < 0:
        game_over = True

    pygame.draw.rect(display, black, [x, y, snake_block, snake_block])
    pygame.display.update()

    # snake speed
    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(1)
 
pygame.quit()
quit()