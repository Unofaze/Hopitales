import config
import pygame

map_width = config.screen_width * 4
map_height = config.screen_height * 4

TAILLE_CASE = 100

# non
def monde_vers_ecran_rect(x, y, largeur, hauteur):
    """
    Convertit un rectangle défini dans le repère monde (centre = (0, 0))
    en pygame.Rect à l'écran en tenant compte du zoom et de la caméra.
    """
    centre_ecran_x = config.screen_width / 2
    centre_ecran_y = config.screen_height / 2

    largeur_zoom = largeur * config.zoom
    hauteur_zoom = hauteur * config.zoom

    # Position du coin haut-gauche à l'écran
    ecran_x = centre_ecran_x + x * config.zoom + config.camera_x
    ecran_y = centre_ecran_y + y * config.zoom + config.camera_y

    return pygame.Rect(
        round(ecran_x),
        round(ecran_y),
        round(largeur_zoom),
        round(hauteur_zoom),
    )


def cameraLimit():
    """
    Empêche la caméra de sortir de la carte en tenant compte du zoom actuel.
    """
    largeur_carte_zoom = map_width * config.zoom
    hauteur_carte_zoom = map_height * config.zoom

    centre_ecran_x = config.screen_width / 2
    centre_ecran_y = config.screen_height / 2

    bord_gauche_initial = centre_ecran_x - largeur_carte_zoom / 2
    bord_droit_initial = centre_ecran_x + largeur_carte_zoom / 2
    bord_haut_initial = centre_ecran_y - hauteur_carte_zoom / 2
    bord_bas_initial = centre_ecran_y + hauteur_carte_zoom / 2

    min_x = config.screen_width - bord_droit_initial
    max_x = -bord_gauche_initial

    min_y = config.screen_height - bord_bas_initial
    max_y = -bord_haut_initial

    if min_x > max_x:
        config.camera_x = (min_x + max_x) / 2
    else:
        config.camera_x = max(min_x, min(max_x, config.camera_x))

    if min_y > max_y:
        config.camera_y = (min_y + max_y) / 2
    else:
        config.camera_y = max(min_y, min(max_y, config.camera_y))


def draw():
    rect_carte = monde_vers_ecran_rect(
        -map_width / 2,
        -map_height / 2,
        map_width,
        map_height,
    )
    pygame.draw.rect(config.screen, (105, 176, 47), rect_carte)

    # Tracage du quadrillage
    pas_zoom = TAILLE_CASE * config.zoom
    if pas_zoom >= 4:
        x_monde = -map_width / 2
        while x_monde <= map_width / 2:
            x_ecran = config.screen_width / 2 + x_monde * config.zoom + config.camera_x
            pygame.draw.line(
                config.screen,
                (255, 0, 0),
                (round(x_ecran), rect_carte.top),
                (round(x_ecran), rect_carte.bottom),
                2,
            )
            x_monde += TAILLE_CASE

        y_monde = -map_height / 2
        while y_monde <= map_height / 2:
            y_ecran = config.screen_height / 2 + y_monde * config.zoom + config.camera_y
            pygame.draw.line(
                config.screen,
                (255, 0, 0),
                (rect_carte.left, round(y_ecran)),
                (rect_carte.right, round(y_ecran)),
                2,
            )
            y_monde += TAILLE_CASE
