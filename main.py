import pygame
import sys
from config import *
from game import SnakeGame
from graphics import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

game = SnakeGame()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                game.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                game.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                game.change_direction((1, 0))
            elif event.key == pygame.K_r and game.game_over:
                game.reset()
    
    game.update()

    screen.fill(BG_COLOR)
    draw_grid(screen)
    draw_snake(screen, game.snake)
    draw_food(screen, game.food)
    draw_score(screen, game.score)

    if game.game_over:
        draw_game_over(screen, game.score)

    pygame.display.flip()
    clock.tick(FPS)
