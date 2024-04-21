import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 10

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the game's speed
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * BLOCK_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * BLOCK_SIZE)) % WINDOW_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WINDOW_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (WINDOW_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main function
def main():
    snake = Snake()
    food = Food()

    while True:
        window.fill(WHITE)
        snake.handle_keys()
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        snake.draw(window)
        food.draw(window)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
