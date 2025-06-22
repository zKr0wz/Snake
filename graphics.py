import pygame
from config import *

def draw_grid(screen):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def draw_snake(screen, snake):
    for segment in snake:
        rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)

def draw_food(screen, food):
    rect = pygame.Rect(food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, rect)

def draw_score(screen, score):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(text, (10, 10))

def draw_game_over(screen, score):
    font = pygame.font.SysFont("arial", 36)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))

    game_over_rect = game_over_text.get_rect(center=(CELL_WIDTH // 2, CELL_HEIGHT // 2 - 30))
    score_rect = score_text.get_rect(center=(CELL_WIDTH // 2, CELL_HEIGHT // 2 + 10))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)

