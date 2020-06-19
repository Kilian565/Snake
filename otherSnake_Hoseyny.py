import sys, pygame, random
pygame.init()
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


size = width, height = 800, 600
BLACK = (0,0,0)
WHITE = (255,255,255)
isRunningUP=0
isRunningDOWN=0
isRunningLEFT=0
isRunningRight=0

screen = pygame.display.set_mode(size)
snake = pygame.image.load('player.bmp').convert()
background = pygame.image.load('liquid.bmp').convert()

food = [(height/32)/2 ,(width/32)/2]
position = snake.get_rect(center=(width/4,height/2))

#_food = pygame.image.load('futter.bmp').convert()

pygame.display.init()
screen.blit(background, (0, 0))
screen.blit(snake, position)
pygame.display.update()

#for x in range(100):                   #animate 100 frames
 #  screen.blit(background, position, position) #erases
  # position = position.move(2, 0)     #move player
   #screen.blit(snake, position)      #draw new player
   #pygame.display.update()            #and show it all
   #pygame.time.delay(100)             #stop the program for 1/10 second
#screen.blit(_food, int(food[0]),int(food[1]))


clock = pygame.time.Clock()
FPS = 10

snk_x = (width/32)/4
snk_y = (height/32)/2

_snake = [                      #ganze schlange
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]






oldkey = pygame.K_RIGHT

#snake = pygame.Rect((0,0), (height/2,width/4))
#image = pygame.Surface((32,32))
#image.fill(WHITE)


while 1:

    #position = snake.get_rect()
    clock.tick(FPS)


    #if _snake[0][0] in [0, height] or _snake[0][1] in [0, width] or _snake[0] in _snake[1:]:
     #  pygame.quit()
      # quit()
    if position >= height or position >= width:
        pygame.quit()

    new_head = [_snake[0][0], _snake[0][1]]

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit()

        if pygame.key.get_pressed()[pygame.K_w]:
            isRunningUP = 1
            isRunningDOWN = 0
            isRunningLEFT = 0
            isRunningRight = 0



        if pygame.key.get_pressed()[pygame.K_d]:
            isRunningUP = 0
            isRunningDOWN = 0
            isRunningLEFT = 0
            isRunningRight = 1


        if pygame.key.get_pressed()[pygame.K_a]:
            isRunningUP = 0
            isRunningDOWN = 0
            isRunningLEFT = 1
            isRunningRight = 0

        if pygame.key.get_pressed()[pygame.K_s]:
            isRunningUP = 0
            isRunningDOWN = 1
            isRunningLEFT = 0
            isRunningRight = 0

    _snake.insert(0, new_head)

    if isRunningUP == 1:
        screen.blit(background, position, position)  # erase
        position = position.move(0, -20)  # move player
        screen.blit(snake, position)
        pygame.display.update()
    if isRunningRight == 1:
        screen.blit(background, position, position)  # erase
        position = position.move(20, 0)  # move player
        screen.blit(snake, position)
        pygame.display.update()
    if isRunningDOWN == 1:
        screen.blit(background, position, position)  # erase
        position = position.move(0, 20)  # move player
        screen.blit(snake, position)
        pygame.display.update()
    if isRunningLEFT == 1:
        screen.blit(background, position, position)  # erase
        position = position.move(-20, 0)  # move player
        screen.blit(snake, position)
        pygame.display.update()

    pygame.display.update()

    #if snake[0] == food:
        #food = None
        #while food is None:
         #   nf = [
         #       random.randint(1, height - 1),
          #      random.randint(1, width - 1)
           # ]
            #food = nf if nf not in snake else None
       # pygame.draw.rect(screen, WHITE, pygame.Rect((0, 0),(food * 16, food * 16),width=0))
    #else:
     #   tail = _snake.pop()
      #  pygame.draw.rect(screen, BLACK, snake)




