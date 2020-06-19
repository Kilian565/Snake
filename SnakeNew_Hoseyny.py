import random
import pygame
import sys

pygame.init()
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

size = width, height = 800/20 , 600/20
RED = (255, 0, 0)
WHITE = (255,255,255)
screen = pygame.display.set_mode((int(size[0]*20),int(size[1]*20)))
clock = pygame.time.Clock()
#background = pygame.image.load('liquid.bmp').convert()
#screen.blit(background, (0, 0))
FPS = 15
#pygame.image.load('player.bmp').convert()


snk_x = width/4
snk_y = height/2

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [height/2, width/2]
pygame.draw.rect(screen,WHITE,pygame.Rect(int(food[1])*20,int(food[0])*20,20,20))


pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key = pygame.K_d))





Running = True

while Running:
    clock.tick(FPS)

    if snake[0][0] in [0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:
        Running = False

    new_head = [snake[0][0], snake[0][1]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            oldkey = event.key
            if event.key == pygame.K_s:
                new_head[0] +=1
            if event.key == pygame.K_w:
                new_head[0] -= 1
            if event.key == pygame.K_a:
                new_head[1] -= 1
            if event.key == pygame.K_d:
                new_head[1] += 1

    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=oldkey))
    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, height - 1),
                random.randint(1, width - 1)
            ]
            food = nf if nf not in snake else None
        pygame.draw.rect(screen,WHITE,pygame.Rect(int(food[1])*20,int(food[0])*20,20,20))
    else:
        tail = snake.pop()
        pygame.draw.rect(screen, RED, pygame.Rect(int(tail[1]) * 20, int(tail[0]) * 20, 20, 20))

    pygame.draw.rect(screen, WHITE, pygame.Rect(int(snake[0][1])*20,int(snake[0][0])*20,20,20))
    pygame.display.update()