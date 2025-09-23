import random
import pygame
import math
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ball Fighter")

clock = pygame.time.Clock()

player_ball_x, player_ball_y = 400, 200
player_vel = 5

cpu_ball_x, cpu_ball_y = 400, 400
cpu_vel = 5

kb_speed = 50
click = False

font = pygame.font.SysFont("comicsans", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((150, 80, 0))

    pygame.draw.circle(screen, (0, 150, 255), (400, 300), 250)
    pygame.draw.circle(screen, (0, 0, 255), (player_ball_x, player_ball_y), 40)
    pygame.draw.circle(screen, (255, 0, 0), (cpu_ball_x, cpu_ball_y), 40)

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_ball_x -= player_vel
    if keys[pygame.K_d]:
        player_ball_x += player_vel
    if keys[pygame.K_w]:
        player_ball_y -= player_vel
    if keys[pygame.K_s]:
        player_ball_y += player_vel

    # Collision
    dx = cpu_ball_x - player_ball_x
    dy = cpu_ball_y - player_ball_y
    distance = math.sqrt(dx ** 2 + dy ** 2)

    # Game over logic (player)
    dxa = player_ball_x - 400
    dya = player_ball_y - 300
    distancea = math.sqrt(dxa ** 2 + dya ** 2)

    # Game over logic (cpu)
    cpu_dx = cpu_ball_x - 400
    cpu_dy = cpu_ball_y - 300
    cpu_distance = math.sqrt(cpu_dx ** 2 + cpu_dy ** 2)

    if distancea > 300:
        screen.blit(font.render("YOU LOSE!", True, (255, 255, 255)), (10, 10))
        print(distancea)
        print("You lose")
        pygame.time.wait(2000)
        pygame.quit()
        exit()
    if cpu_distance > 300:
        screen.blit(font.render("YOU WIN!", True, (255, 255, 255)), (10, 10))
        print(cpu_distance)
        print("You win")
        pygame.time.wait(2000)
        pygame.quit()
        exit()

    if cpu_distance > 230 and not click:
        cpu_dx /= cpu_distance
        cpu_dy /= cpu_distance
        cpu_ball_x += cpu_dx * cpu_vel
        cpu_ball_y += cpu_dy * cpu_vel
    else:
        if cpu_ball_y > player_ball_y:
            cpu_ball_y -= cpu_vel
            if max(cpu_ball_y, player_ball_y) - min(cpu_ball_y, player_ball_y) < 30 and random.randint(1, 2) != 1:
                player_ball_y -= kb_speed
        elif cpu_ball_y < player_ball_y:
            cpu_ball_y += cpu_vel
            if max(cpu_ball_y, player_ball_y) - min(cpu_ball_y, player_ball_y) < 30 and random.randint(1, 2) != 1:
                player_ball_y += kb_speed

        if cpu_ball_x < player_ball_x:
            cpu_ball_x += cpu_vel
            if max(cpu_ball_x, player_ball_x) - min(cpu_ball_x, player_ball_x) < 30 and random.randint(1, 2) != 1:
                player_ball_x += kb_speed
        elif cpu_ball_x > player_ball_x:
            cpu_ball_x -= cpu_vel
            if max(cpu_ball_x, player_ball_x) - min(cpu_ball_x, player_ball_x) < 30 and random.randint(1, 2) != 1:
                player_ball_x -= kb_speed

    if distance != 0:
        dx /= distance
        dy /= distance

    # Mouse click
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dxm = cpu_ball_x - mouse_x
    dym = cpu_ball_y - mouse_y
    distancem = (dxm ** 2 + dym ** 2) ** 0.5

    if distance <= 80 and pygame.mouse.get_pressed()[0] and distancem <= 80:
        if random.randint(1, 30) == 1:
            cpu_ball_x += dx + 2 * kb_speed
            cpu_ball_y += dy + 2 * kb_speed
        cpu_ball_x += dx + 1 * kb_speed
        cpu_ball_y += dy + 1 * kb_speed
        click = True
    click = False

    pygame.display.update()
    clock.tick(60)
    print(distancea)
