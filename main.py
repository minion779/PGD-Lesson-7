import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))

screen.fill((0,255,0))
pygame.display.update()

candyCrush = pygame.image.load("candy.jpg")
ludo = pygame.image.load("ludo.png")
subwaySurfers = pygame.image.load("subway.png")
templeRun = pygame.image.load("temple.png")

screen.blit(candyCrush, (150,50))
screen.blit(ludo, (150,150))
screen.blit(subwaySurfers, (150, 250))
screen.blit(templeRun, (150, 350))

font = pygame.font.SysFont("Times New Roman", 36)
text1 = font.render("Subway Surfers",True, (0,0,0))
screen.blit(text1, (350,70))

text2 = font.render("Candy Crush", True, (0,0,0))
screen.blit(text2, (350,170))

text3 = font.render("Temple Run", True, (0,0,0))
screen.blit(text3, (350,270))

text4 = font.render("Ludo", True, (0,0,0))
screen.blit(text4, (350,370))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,0), pos, 10,0)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,0), pos2, 10,0)
            pygame.draw.line(screen, (0,0,0), pos, pos2, 5)
            pygame.display.update()