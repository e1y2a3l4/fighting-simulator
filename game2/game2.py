import pygame
import random

pygame.mixer.init()
sound = pygame.mixer.Sound ("res/ouch-208265.mp3")
pygame.init()

#text
color = (255, 0 , 0)
font = pygame.font.Font("freesansbold.ttf" , 25)
text = font.render("GAME OVVVVVEEEEEEERRRRRRRRRRRRRRRRRRRRR!" , True, color)
text_rect = text.get_rect()
text_rect.center = (100, 600)

#blue player
player2 = [pygame.image.load("res/pixelart/pixil-frame-0.png"),
           pygame.image.load("res/pixelart/pixil-frame-1.png"),
           pygame.image.load("res/pixelart/pixil-frame-2.png"),
           pygame.image.load("res/pixelart/pixil-frame-3.png"),
           pygame.image.load("res/pixelart/pixil-frame-4.png")]

screen = pygame.display.set_mode((0, 0))
#red player
player_img = [pygame.image.load("res/pixilart-frames/pixil-frame-0.png"),
              pygame.image.load("res/pixilart-frames/pixil-frame-1.png"),
              pygame.image.load("res/pixilart-frames/pixil-frame-2.png"),
              pygame.image.load("res/pixilart-frames/pixil-frame-3.png"),
              pygame.image.load("res/pixilart-frames/pixil-frame-4.png")]
#cloud animation
screen2 = [pygame.image.load("res/pixilart-frames(1)/pixil-frame-0.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-1.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-2.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-3.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-4.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-5.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-6.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-7.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-8.png"),
           pygame.image.load("res/pixilart-frames(1)/pixil-frame-9.png")]

exit = pygame.image.load("res/exit.png")

#blue heart
blue_heart = pygame.image.load("res/lev.png")

#red heart
red_heart = pygame.image.load("res/lev2.png")
blue_life = 3
red_life = 3

atack = False
atack2 = False

#animation of calouds
for c in range(len(screen2)):
    screen2[c] = pygame.transform.scale(screen2[c], (1920, 1080))

#red player animation
for i in range(len(player_img)):
    player_img[i] = pygame.transform.scale(player_img[i], (250, 200))

#red player rect
player_rect = player_img[0].get_rect()
player_rect.x = random.randint(1, 1273)
player_rect.y = random.randint(-9, 671)

text_rect = text.get_rect()
text_rect.x = 460
text_rect.y = 100

#blue player animation
for i in range(len(player2)):
    player2[i] = pygame.transform.scale(player2[i], (250, 200))

#blue player rect
player2_rect = player2[0].get_rect()
player2_rect.x = random.randint(1, 1273)
player2_rect.y = random.randint(-9, 671)

#right sword
herev1 = pygame.image.load("res/sword.png")
herev1 = pygame.transform.scale(herev1, (250, 250))
herev1_rect = herev1.get_rect()
herev1_rect.x = player_rect.x
herev1_rect.y = player_rect.y
herev1_rect.w = 250
herev1_rect.h = 250

#left sword
herev2 = pygame.image.load("res/play.png")
herev2 = pygame.transform.scale(herev2, (250, 250))
herev2_rect = herev2.get_rect()
herev2_rect.x = 500
herev2_rect.y = 550

#blue heart y and x and rect and size
lev_rect = blue_heart.get_rect()
lev_rect.x = 50
lev_rect.y = 50
blue_heart = pygame.transform.scale(blue_heart, (100, 100))

#red heart rect + y and x and size
lev2_rect = red_heart.get_rect()
lev2_rect.x = 1200
lev2_rect.y = 50
red_heart = pygame.transform.scale(red_heart, (100, 100))

#the animation control code
animation_index = 0
animation_index_2 = 0
animation_index_screen = 0

screen_number = 1

exit = pygame.transform.scale(exit, (200, 200))
exit_rect = exit.get_rect()
exit_rect.y = 0
exit_rect.x = 0

play = pygame.image.load("res/png.png")
screen1st = pygame.image.load("res/play2.png")
play = pygame.transform.scale(play, (500, 250))
play_rect = play.get_rect()
play_rect.x = 600
play_rect.y = 400

#the "while"
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if screen_number == 0:
        keys = pygame.key.get_pressed()

        herev1_rect.x = player_rect.x
        herev1_rect.y = player_rect.y

        herev2_rect.x = player2_rect.x
        herev2_rect.y = player2_rect.y

        if atack == True:
            animation_index += 1
            if animation_index == 10:
                animation_index = 0
                atack = False

        if atack2 == True:
            animation_index_2 += 1
            if animation_index_2 == 10:
                animation_index_2 = 0
                atack2 = False

        animation_index_screen += 1
        if animation_index_screen == 36:
            animation_index_screen = 0



        if keys[pygame.K_a]:
            player_rect.x -= 14
        if keys[pygame.K_d]:
            player_rect.x += 14
        if keys[pygame.K_s]:
            player_rect.y += 14
        if keys[pygame.K_w]:
            player_rect.y -= 14
        if keys[pygame.K_f]:
            atack = True

        if keys[pygame.K_LEFT]:
            player2_rect.x -= 14
        if keys[pygame.K_RIGHT]:
            player2_rect.x += 14
        if keys[pygame.K_DOWN]:
            player2_rect.y += 14
        if keys[pygame.K_UP]:
            player2_rect.y -= 14
        if keys[pygame.K_RSHIFT]:
            atack2 = True


        if player_rect.x < 0:
            player_rect.x += 14
        if player_rect.y < -10:
            player_rect.y += 14
        if player_rect.y > 672:
            player_rect.y -= 14
        if player_rect.x > 1400:
            player_rect.x -= 14

        if player2_rect.x < -100:
            player2_rect.x += 14
        if player2_rect.y < -10:
            player2_rect.y += 14
        if player2_rect.y > 672:
            player2_rect.y -= 14
        if player2_rect.x > 1300:
            player2_rect.x -= 14

        if herev1_rect.colliderect(player2_rect) and keys[pygame.K_f]:
            blue_life -= 1
            player2_rect.x += 400
            sound.play()
        if herev2_rect.colliderect(player_rect) and keys[pygame.K_RSHIFT]:
            red_life -= 1
            player_rect.x -= 400
            sound.play()





        screen.blit(screen2[animation_index_screen // 4], (0, 0))
        screen.blit(player_img[animation_index // 2], player_rect)
        screen.blit(player2[animation_index_2 // 2], player2_rect)
        #screen.blit(herev1, herev1_rect)
        #screen.blit(herev2, herev2_rect)

        for i in range(blue_life):
            screen.blit(blue_heart, (lev_rect.x + i * 100, lev_rect.y))
        for i in range(red_life):
            screen.blit(red_heart, (lev2_rect.x + i * 100, lev2_rect.y))
        if blue_life <0 or blue_life==0:
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            screen_number = 1
            blue_life = 3
            red_life = 3
            player_rect.x = random.randint(1, 1273)
            player_rect.y = random.randint(-9, 671)
            player2_rect.x = random.randint(1, 1273)
            player2_rect.y = random.randint(-9, 671)

        if red_life <0 or red_life==0:
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            screen_number = 1
            blue_life = 3
            red_life = 3
            player_rect.x = random.randint(1, 1273)
            player_rect.y = random.randint(-9, 671)
            player2_rect.x = random.randint(1, 1273)
            player2_rect.y = random.randint(-9, 671)


        clock.tick(30)
        pygame.display.flip()

    if screen_number == 1 :


        screen.blit (screen1st, (0, 0))
        screen.blit (play, (600, 400))
        screen.blit(exit, (0, 0))
        screen1st = pygame.transform.scale(screen1st, (1980, 1080))

        mouse_clicked = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if play_rect.collidepoint((mouse_pos[0], mouse_pos[1])):
            if mouse_clicked[0]:
                screen_number = 0

        if exit_rect.collidepoint((mouse_pos[0], mouse_pos[1])):
            if mouse_clicked[0]:
                running = False

        pygame.display.flip()