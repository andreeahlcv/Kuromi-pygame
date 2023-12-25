import pygame
import random
import time
import os
pygame.font.init()

width, height = 800, 600
window= pygame.display.set_mode((width, height))
pygame.display.set_caption("Kuromi Game")

background=pygame.transform.scale(pygame.image.load("kuromi.jpeg"), (width, height))
playerr_width=40
player_height=60
player_velocity=4
star_width=10
star_height=20
star_velocity=4
font=pygame.font.SysFont("arial", 30)

def draw(player, elapsed_time, stars):
    window.blit(background, (0, 0))
    time_text=font.render(f"Time: {(elapsed_time)}s", 1, "white")
    window.blit(time_text, (10, 10))

    pygame.draw.rect(window, "black", player)

    for star in stars:
        pygame.draw.rect(window, "white", star)

    pygame.display.update() 

def main():
    run=True

    player=pygame.Rect(150, height-player_height,playerr_width, player_height,)
    clock=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0

    star_add_increments=2000
    star_count=0

    stars=[]
    hit=False

    while run:
        star_count += clock.tick(50)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increments:
            for _ in range(4):
                star_x = random.randint(0, width - star_width)
                star = pygame.Rect(star_x, - star_height, star_width, star_height)
                stars.append(star)

            star_add_increments = max(150, star_add_increments - 50)
            star_count = 0 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_velocity >=0:
            player.x -= player_velocity
        if keys[pygame.K_RIGHT] and player.x + player_velocity + playerr_width <= width:
            player.x += player_velocity

        for star in stars[:]:
            star.y += star_velocity
            if star.y > height:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text=font.render("OOPSY...ITS TIME TO TRY AGAIN HUN", 1, "black")
            window.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2 ))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()