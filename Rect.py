import pygame,sys
import pygame.event as game_events
import pygame.locals as game_globals
import random
pygame.init()

window = pygame.display.set_mode((900,700))

pygame.display.set_caption('REZA.1391')

basicFont = pygame.font.SysFont('Comic Sans MS', 40)

playerx = 300
playery = 600
movespeed = 0.5
left = False
right = False
yp = False
down = False

counter = 0
lst = []
x1 = 0
y1= 0
score = 0
while True:
    window.fill((0,0,255))
    player = pygame.draw.rect(window , (255,255,0) , (playerx,playery,50,50),0)

    if counter == 1000:
        x = random.randint(0,900)
        y = random.randint(0,700)
        lst.append((x,y))
        counter = 0

    sefid = pygame.draw.rect(window,(255,255,255), (x1,y1,30,30), 0)
    x1 += 0.2
    y1 += 0.2
    if x1 > 700:
        x1 = 0
    if y1 > 900:
        y1 = 0

    for i in lst:
        pygame.draw.rect(window, (0,255,0), (i[0],i[1],30,30),0)
    
    for event in game_events.get():
        if event.type == game_globals.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_a:
                left = True
            if event.key==pygame.K_d:
                right = True
            if event.key==pygame.K_w:
                yp = True
            if event.key == pygame.K_s:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right =  False
            if event.key == pygame.K_w:
                yp = False
            if event.key == pygame.K_s:
                down = False


    if left == True and playerx > 0:
        playerx -= movespeed
    if right == True and playerx+50 <900:
        playerx += movespeed
    if yp == True and playery > 0:
        playery -= movespeed
    if down == True and playery+50 < 700:
        playery += movespeed

    counter += 1
            
    for i in lst:
        if player.colliderect((i[0],i[1],30,30)):
            lst.remove(i)
            score += 1
    if player.colliderect(sefid):
        score -= 1
        x1 = 0
        y1 = 0
    text = basicFont.render(str(score), True, (255,255,255), (0,0,0))
    window.blit(text, (0,0))
    pygame.display.update()


