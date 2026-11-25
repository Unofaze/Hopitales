import config
import game_map
import hospital
import ecran_accueil
import pygame

dragging = False

scene_en_cours = config.scenes[0]  # Commence par la scène du menu
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    if scene_en_cours == "menu":
        ecran_accueil.draw()

    if scene_en_cours == "third_person":

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            dragging = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            dragging = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            dx, dy = event.rel
            config.camera_x += dx
            config.camera_y += dy
            game_map.cameraLimit()

        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                config.zoom = min(config.ZOOM_MAX, round(config.zoom + config.ZOOM_PAS, 2))
            elif event.y < 0:
                config.zoom = max(config.ZOOM_MIN, round(config.zoom - config.ZOOM_PAS, 2))

        game_map.cameraLimit()

        config.screen.fill((0, 0, 0))

        game_map.draw()
        hospital.draw()

    pygame.display.flip()

pygame.quit()