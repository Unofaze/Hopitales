import config
import game_map
import hospital
import ecran_accueil
import pygame
import arrivée_patients

dragging = False
scene_en_cours = "menu"
hopital_manager = arrivée_patients.GestionnaireHospitalier(10000) # 10000 millisecondes = 10 secondes (temps entre l'arrivée de chaque patient)

gameRunning = True
while gameRunning:
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
                elif event.key == pygame.K_a:
                    hopital_manager.assigner_patient_a_chambre(hopital_manager.premiere_chambre_libre())

    if scene_en_cours != "menu":
        hopital_manager.mettre_a_jour_accueil()

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
        hopital_manager.draw_salle_d_attente()


    pygame.display.flip()

pygame.quit()