import pygame
from .models import Snake, Food

class GameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                    self.snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                    self.snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                    self.snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                    self.snake.direction = 'RIGHT'

    def update(self):
        self.snake.move()
        if self.snake.eat(self.food.position):
            self.food.generate()

    def render(self):
        self.screen.fill((0, 0, 0))
        for pos in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 20, 20))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], 20, 20))
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(10)