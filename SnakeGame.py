import pygame

pygame.init()
display = pygame.display.set_mode((900,600))
pygame.display.set_caption('Snake game by kiyohiro')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)

game_over = False

# initial position
x = 300
y = 300

# starts without movement 
x_change = 0       
y_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 10
                x_change = 0

    x += x_change
    y += y_change
    display.fill(white)

    pygame.draw.rect(display, black, [x, y, 15, 15 ])
    pygame.display.update()

    # snake speed
    clock.tick(20)
 
pygame.quit()
quit()