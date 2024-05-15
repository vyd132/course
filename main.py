import random
import time

import pygame

screen=pygame.display.set_mode([500,500])

a=pygame.rect.Rect([0,0,500,500])

dots=15
dotx=0
dot_list=[]

for dot in range(dots):
    object = random.randint(0, 500)
    dot_list.append(object)

while True:
    time.sleep(1)
    del dot_list[0]
    object = random.randint(0, 500)
    dot_list.append(object)

    screen.fill([0,0,0])
    for y in dot_list:
        pygame.draw.circle(screen, [random.randint(0,255), 255, random.randint(0,255)], [dotx, y], 4)
        dotx += a.w / (dots - 1)
    dotx=0
    pygame.display.flip()



