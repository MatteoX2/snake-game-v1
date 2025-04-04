import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 10
FPS = 10

GREY = (84, 85, 85)
WHITE = (255, 255, 255)
WHITE = (255, 255, 255)
YELLOW = (223, 255, 72)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE BY @MATTEOX")

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

snake = [(200, 200), (220, 200), (240, 200)]
food = (500, 500)

direction = "right"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!= "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction!= "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction!= "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction!= "left":
                direction = "right"

    head = snake[-1]
    if direction == "up":
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == "down":
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == "left":
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == "right":
        new_head = (head[0] + BLOCK_SIZE, head[1])
    snake.append(new_head)

    if snake[-1] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)

    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
        snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
        snake[-1] in snake[:-1]):
        pygame.quit()
        sys.exit()

    screen.fill(GREY)
    for pos in snake:
        pygame.draw.rect(screen, YELLOW, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, WHITE, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    text = font.render(f"MY SCORE: {len(snake)}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)
