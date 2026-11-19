import config
import game_map
import hospital
import pygame

dragging = False

gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            dragging = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            dragging = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            dx, dy = event.rel    
            config.camera_x += dx
            config.camera_y += dy

    config.screen.fill((0, 0, 0))

    game_map.draw()
    hospital.draw()
    
    

    pygame.display.flip()

pygame.quit()