import random
from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

player_paddle_y = 0
cpu_paddle_y = 0
ball_x = 400
ball_y = 300
speed = 6
ball_dir_x = random.randint(-1, 1)
ball_dir_y = random.randint(-1, 1)
cpu_random_choice = 1

player_score = 0
cpu_score = 0
timer_min = 2
timer_sec = 59
timer_fps = 60
ball_color = (255, 0, 0)

font = pygame.font.Font("font/Acme 9 Regular.ttf", 18)
font2 = pygame.font.Font("font/Acme 9 Regular.ttf", 20)

win_message_font = pygame.font.SysFont("Arial", 50)

waiting = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Timer
    timer_fps -= 1

    if timer_fps == 0:
        timer_fps = 60
        timer_sec -= 1

    if timer_sec == 0:
        timer_sec = 59
        timer_min -= 1

    if timer_min < 0:
        timer_min = 0
        timer_sec = 0

        # Pick winner text
        if player_score > cpu_score:
            winner = "Player Wins!"
        elif cpu_score > player_score:
            winner = "CPU Wins!"
        else:
            winner = "Draw!"

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.fill((0, 200, 255))
            screen.blit(win_message_font.render(winner, True, (0, 0, 0)), (330, 200))
            screen.blit(
                win_message_font.render("Press SPACE to restart", True, (0, 0, 0)),
                (200, 300),
            )
            pygame.display.update()

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                player_paddle_y = cpu_paddle_y = 0
                ball_x, ball_y = 400, 300
                ball_dir_x = random.choice([-1, 1])
                ball_dir_y = random.choice([-1, 1])
                player_score = cpu_score = 0
                timer_min, timer_sec, timer_fps = 2, 59, 60
                waiting = False

    # Ball movement
    if ball_dir_x == 0:
        ball_dir_x = random.randint(-1, 1)
    if ball_dir_y == 0:
        ball_dir_y = random.randint(-1, 1)
    if ball_y <= 30 or ball_y >= 690:
        ball_dir_y *= -1
    if ball_x <= 30 or ball_x >= 1250:
        ball_dir_x *= -1

    # Collisions
    if ball_x <= 55 and player_paddle_y <= ball_y <= player_paddle_y + 130:
        if ball_color == (255, 255, 0):
            player_score += 2
            ball_color = (255, 0, 0)
        elif ball_color == (0, 0, 255):
            cpu_score -= random.randint(1, 3)
            ball_color = (255, 0, 0)
        elif ball_color == (255, 0, 255):
            cpu_score = ((cpu_score + 49) // 50) * 50
            ball_color = (255, 0, 0)
        else:
            player_score += 1
        ball_x *= -1
        ball_dir_x *= -1
        ball_x = 56
    elif ball_x >= 1225 and cpu_paddle_y <= ball_y <= cpu_paddle_y + 130:
        cpu_score += 1
        ball_x *= -1
        ball_dir_x *= -1
        ball_x = 1224

    # CPU Logic
    if ball_y > cpu_paddle_y + 25 and ball_x > random.randint(930, 1050):
        cpu_paddle_y += 40 * clock.get_time() * 0.01
        if cpu_paddle_y >= 470:
            cpu_paddle_y = 470
    elif ball_y < cpu_paddle_y + 25 and ball_x > random.randint(950, 1250):
        cpu_paddle_y -= 40 * clock.get_time() * 0.01
        if cpu_paddle_y <= 0:
            cpu_paddle_y = 0

    screen.fill((20, 160, 133))
    pygame.draw.rect(screen, (38, 185, 154), (640, 0, 1280, 720))
    pygame.draw.rect(screen, (255, 255, 255), (0, player_paddle_y, 25, 130))
    pygame.draw.rect(screen, (255, 255, 255), (1255, cpu_paddle_y, 25, 130))
    pygame.draw.circle(screen, (0, 255, 255), (640, 360), 100)
    pygame.draw.line(screen, (255, 255, 255), (640, 0), (640, 720), 2)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), 30)
    screen.blit(
        font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255)), (10, 10)
    )
    screen.blit(font2.render(f"{player_score}", True, (255, 255, 255)), (320, 10))
    screen.blit(font2.render(f"{cpu_score}", True, (255, 255, 255)), (960, 10))
    screen.blit(font2.render(f"{timer_min}", True, (255, 255, 255)), (575, 10))
    screen.blit(font2.render(f"{timer_sec}", True, (255, 255, 255)), (685, 10))
    screen.blit(font2.render(":", True, (255, 255, 255)), (660, 10))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_paddle_y -= 40 * clock.get_time() * 0.01
        if player_paddle_y <= 0:
            player_paddle_y = 0
    elif keys[pygame.K_DOWN]:
        player_paddle_y += 40 * clock.get_time() * 0.01
        if player_paddle_y >= 590:
            player_paddle_y = 590

    ball_x -= speed * ball_dir_x
    ball_y += speed * ball_dir_y

    pygame.display.update()
    clock.tick(60)
