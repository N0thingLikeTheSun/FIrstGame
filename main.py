"""First Game"""
import pygame


Max_X=1550
Max_Y=870
Img_Size=150
close_game=False
bg_color=(0,0,0)

pygame.init()
screen = pygame.display.set_mode((Max_X,Max_Y))
pygame.display.set_caption("Naruto")

hero=pygame.image.load("naruto.jpg").convert()
hero=pygame.transform.scale(hero,(Img_Size,Img_Size))

x=450
y=210

move_right=False
move_left=False
move_up=False
move_down=False

#------Main-------
while close_game == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #Проверка на нажатие кнопки, и включение движения\выход из игры
            if event.key == pygame.K_ESCAPE:
                close_game = True
            if event.key == pygame.K_DOWN:
                move_down=True
            if event.key == pygame.K_UP:
                move_up=True
            if event.key == pygame.K_LEFT:
                move_left=True
            if event.key == pygame.K_RIGHT:
                move_right=True

        if event.type == pygame.KEYUP:  # Проверка на нажатие кнопки, и включение движения\выход из игры
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
    if move_down:   #Блок выполнения движения
        y += 1
        if y > Max_Y-Img_Size:
            y=Max_Y-Img_Size
    if move_up:
        y-=1
        if y<0:
            y=0
    if move_left:
        x-=1
        if x<0:
            x=0
    if move_right:
        x+=1
        if x>Max_X-Img_Size:
            x=Max_X-Img_Size
    if event.type == pygame.MOUSEBUTTONDOWN:
        x,y=event.pos
    screen.fill(bg_color)
    screen.blit(hero, (x,y))
    pygame.display.flip()


