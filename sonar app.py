import pygame
import math
import time



pygame.init()

font = pygame.font.SysFont(None, 67)

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("goooooon")

wave_surf = pygame.Surface((600, 600), pygame.SRCALPHA)
echo_surf = pygame.Surface((600, 600), pygame.SRCALPHA)

echo_wave = False


bg = pygame.image.load("background.png").convert()
bg = pygame.transform.scale(bg, (600,600))

obj = pygame.image.load("object1.png").convert_alpha()
obj = pygame.transform.scale(obj, (50, 50))
obj_rect = obj.get_rect(center=(300,300))

spawn = pygame.image.load("spawn.png").convert_alpha()
spawn = pygame.transform.scale(spawn, (25, 25))
spawn_rect = spawn.get_rect()


clock=pygame.time.Clock()

running=True

wave_radius = 0

wave_speed = 2

echo_rad = 0

echo_speed = 2


last_time = pygame.time.get_ticks()



summon = False
inc=True

while running:

    wave_surf.fill((0,0,0,0))
    echo_surf.fill((0,0,0,0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            summon = True
            spawn_rect.center = event.pos
            spawncenter= spawn_rect.center
            spawntime = pygame.time.get_ticks()

    pygame.draw.circle(wave_surf, (0, 0, 0, 200), obj_rect.center, wave_radius, 5)
    


    screen.blit(bg, (0,0))
    screen.blit(obj, obj_rect)
    screen.blit(wave_surf, (0, 0))

    if inc==True:
        wave_radius += wave_speed


    elif inc==False:
        wave_radius -= wave_speed

    
    if echo_wave==True:
        pygame.draw.circle(echo_surf, (0, 0, 0, 150), spawncenter, echo_rad, 5)
    
        screen.blit(echo_surf, (0,0))
        echo_rad += echo_speed

        if ((dist-7)-echo_rad)>1 and ((dist-7)-echo_rad) <5:
            echo_wave=False

    

    if wave_radius > 415:
        inc = False

    if wave_radius < 17:
        inc = True
        circle_time_start = pygame.time.get_ticks()





    if summon == True:
        screen.blit(spawn, (spawncenter))
        if pygame.time.get_ticks() - spawntime > 3000:
            summon = False

        dist = math.hypot(spawncenter[0]-300, spawncenter[1]-300)

        if (dist-wave_radius)>1 and (dist-wave_radius) <5:
            current= pygame.time.get_ticks()/1000
            totaltime=current-circle_time_start
            
            echo_rad=0
            pygame.draw.circle(echo_surf, (0, 0, 0, 150), spawncenter, echo_rad, 5)

            echo_wave = True            

        

    




    
    pygame.display.flip()

    
    clock.tick(60)  # limits FPS to 60


pygame.quit()
