import config
import game_map
import hospital
import ecran_accueil
import pygame
import arrivée_patients

dragging = False
scene_en_cours = "menu"

# Liste de patients (avec un patient de test pour éviter un écran vide)
liste_patients = [arrivée_patients.Patient("")]

gameRunning = True
while gameRunning:
    # 1. TOUS les événements doivent être indentés dans cette boucle for
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

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

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene_en_cours = "first_person"

        elif scene_en_cours == "first_person":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene_en_cours = "third_person"

    # 2. Affichage de la scène active
    if scene_en_cours == "menu":
        ecran_accueil.draw()
        if ecran_accueil.est_clique_play():
            scene_en_cours = "third_person"

    elif scene_en_cours == "third_person":
        game_map.cameraLimit()
        config.screen.fill((0, 0, 0))
        game_map.draw()
        hospital.draw()

    elif scene_en_cours == "first_person":
        config.screen.fill((255, 255, 255))
        arrivée_patients.draw(liste_patients)

    pygame.display.flip()

pygame.quit()
