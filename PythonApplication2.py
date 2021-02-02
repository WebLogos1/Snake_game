#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 0, 0), block_rect)

    def move_snake(self):
        if self.new_block == True:
           body_copy = self.body[:]
           body_copy.insert(0, body_copy[0] + self.direction)
           self.body = body_copy[:]
           self.new_block = False
        else:
              body_copy = self.body[:-1]
              body_copy.insert(0, body_copy[0] + self.direction)
              self.body = body_copy[:]
    def add_block(self):
        self.new_block = True

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (50, 0, 255), fruit_rect)
    def randomize(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruits = Fruit()
    def update(self):
         self.snake.move_snake()
         self.check_coll()
         self.check_fail()

    def draw_elements(self):
        self.fruits.draw_fruit()
        self.snake.draw_snake()
    def Movement(self):
         if event.key == pygame.K_UP:
          if main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
         if event.key == pygame.K_DOWN:
          if main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
         if event.key == pygame.K_RIGHT:
          if main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
         if event.key == pygame.K_LEFT:
          if main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
    def check_coll(self):
        if self.fruits.pos == self.snake.body[0]:
            self.fruits.randomize()
            self.snake.add_block()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num:
            self.game_over()
        for block in self.snake.body[1:]:
         if block == self.snake.body[0]:
           self.game_over()
    def game_over(self):
         pygame.quit()
         sys.exit()
    

pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_num * cell_size, cell_num * cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           main_game.game_over()
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
           main_game.Movement()
        screen.fill((75, 225, 50))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)
