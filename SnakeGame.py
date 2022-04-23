import pygame

pygame.init()
display = pygame.display.set_mode((900,600))
pygame.display.update()
pygame.display.set_caption('Snake game by kiyohiro')

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()