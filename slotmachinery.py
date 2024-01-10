import pygame
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 624))

pygame.display.set_caption("Slot Machine")

randomNumber1 = 0
randomNumber2 = 0
randomNumber3 = 0

appleImg = pygame.image.load("Images/apple.png")
bananaImg = pygame.image.load("Images/banana.png")
strawberryImg = pygame.image.load("Images/strawberry.png")
orangeImg = pygame.image.load("Images/orange.png")
grapesImg = pygame.image.load("Images/grapes.png")
slot_machine = pygame.image.load("Images/slotmachine.png")

fruits = [appleImg, bananaImg, strawberryImg, orangeImg, grapesImg]

Img1X = 225
Img2X = 345
Img3X = 483
Img1Y = 600
Img2Y = 600
Img3Y = 600
ImgYChange = -3

# cooldown = 1
spaceCounter = 0

font = pygame.font.Font(None, 60)

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if spaceCounter == 3:
                    spaceCounter = 3
                else:
                    spaceCounter += 1

    if Img1Y > -128 and spaceCounter < 1:
        Img1Y += ImgYChange
    if Img1Y == 0 and spaceCounter < 1:
        Img1Y = 600
        randomNumber1 = random.randint(0, len(fruits)-1)
    elif spaceCounter == 1:
        Img1Y = 280

    if Img2Y > -128 and spaceCounter < 2:
        Img2Y += ImgYChange
    if Img2Y == 0 and spaceCounter < 2:
        Img2Y = 600
        randomNumber2 = random.randint(0, len(fruits)-1)
    elif spaceCounter == 2:
        Img2Y = 280

    if Img3Y > -128 and spaceCounter < 3:
        Img3Y += ImgYChange
    if Img3Y == 0 and spaceCounter < 3:
        Img3Y = 600
        randomNumber3 = random.randint(0, len(fruits)-1)
    elif spaceCounter == 3:
        Img3Y = 280

    screen.blit(fruits[randomNumber1], (Img1X, Img1Y))
    screen.blit(fruits[randomNumber2], (Img2X, Img2Y))
    screen.blit(fruits[randomNumber3], (Img3X, Img3Y))
    screen.blit(slot_machine, (0,0))

    if spaceCounter == 3 and randomNumber1 == randomNumber2 == randomNumber3:
        congrats_text = font.render("You win!", True, (255, 255, 255))
        text_rect = congrats_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(congrats_text, text_rect.move(0, -congrats_text.get_height() // 2))
    elif spaceCounter == 3:
        lose_text = font.render("You lose!", True, (255,255,255))
        text_rect = lose_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(lose_text, text_rect.move(0, -lose_text.get_height() // 2))
    pygame.display.update()

pygame.quit
