import random
import time

import pygame

screen=pygame.display.set_mode([500,500])

a=pygame.rect.Rect([0,0,500,500])

dots=100
dotx=0
dot_list=[]
liney=1
x=a.w / (dots - 1)


object = 250

for dot in range(dots):
    object+=(random.randint(-50,50))
    dot_list.append(object)


while True:
    time.sleep(1/10)
    copy=dot_list.copy()
    del dot_list[0]
    copy[len(dot_list)] += (random.randint(-50,50))
    dot_list.append(copy[len(dot_list)])
    if dot_list[len(dot_list)-1]<0:
        for y in range(len(dot_list)):
            dot_list[y]+=50
    if dot_list[len(dot_list)-1]-1>500:
        for y in range(len(dot_list)):
            dot_list[y]-=50

    screen.fill([0,0,0])
    print(dot_list[len(dot_list)-1])
    for y in dot_list:
        pygame.draw.circle(screen, [20, 255, 10], [dotx, y], 4)
        dotx += x
    dotx = 0
    for y in range(len(dot_list)-1):
        pygame.draw.line(screen, [20, 255, 10], [dotx, dot_list[y]],[dotx + x, dot_list[y+1]],2)
        dotx += x
    dotx=0
    pygame.display.flip()



