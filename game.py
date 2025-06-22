import random
from config import *

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(CELL_WIDTH // 2, CELL_HEIGHT // 2)]
        self.direction = (0, 1) # start moving up
        self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        while True:
            self.food = (random.randint(0, CELL_WIDTH -1), random.randint(0, CELL_HEIGHT -1))
            if self.food not in self.snake:
                break

    def change_direction(self, new_direction):
        # Prevent the snake from reversing directly
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        # Check collision with walls
        if not (0 <= new_head[0] < CELL_WIDTH and 0 <= new_head[1] < CELL_HEIGHT):
            self.game_over = True
            return

        # Check collision with self
        if new_head in self.snake:
            self.game_over = True
            return

        # Move snake
        self.snake.insert(0, new_head)

        # Check food collision
        if new_head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()
