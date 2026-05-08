import pygame
import os
pygame.font.init()
WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle")

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)

BORDER = pygame.Rect(WIDTH//2 - 5,0,10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)

SPACE_IMAGE = pygame.image.load(os.path.join("Assets","space.png"))
SPACE = pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT))

def drawWindows(red,yellow,red_bullets, yellow_bullets, red_health, yellow_health):
    screen.blit(SPACE, (0,0))
    pygame.draw.rect(screen, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health:" + str(red_health),1,WHITE)
    screen.blit(red_health_text,(700,10))
    screen.blit(RED_SPACESHIP, (red.x, red.y))

    yellow_health_text = HEALTH_FONT.RENDER("Health:" + str(yellow_health),1, WHITE)
    screen.blit(yellow_health_text, (10,10))
    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(screen,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,YELLOW,bullet)
    
    pygame.display.update()

def drawWinner(text):
    drawText = WINNER_FONT.render(text, 1, WHITE)
    screen.blit(drawText, (WIDTH/2 - drawText.get_width() / 2, HEIGHT / 2 - drawText.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)

def yellowHandleMovement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def redHandleMovement(keys_pressed, red):
    if keys_pressed[pygame.K_j] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_l] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_i] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_k] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL

def handleBullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)

def main():
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x, yellow.y, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_m and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y, 10, 5)
                    red_bullets.append(bullet)
            if event.type == RED_HIT:
                red_health -= 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1















