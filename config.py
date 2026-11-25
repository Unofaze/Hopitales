import pygame

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))

camera_x, camera_y = 0, 0

zoom = 1.0
ZOOM_MIN = 0.5
ZOOM_MAX = 2.0
ZOOM_PAS = 0.1

scenes = [
    "menu",
    "first_person",
    "third_person",
]


def afficher_texte(texte, x, y, maxi, couleur):
    """
    Cette fonction permet d'afficher du texte dans une fenêtre Pygame à partir d'une position donnée (x, y). Si une ligne de texte dépasse
    la largeur de la fenêtre, elle est automatiquement coupée et continuée à la ligne suivante.

    Paramètres :
    -----------
        texte(str) : Le texte à afficher.

        x(int) : La position en pixels sur l'axe des abscisses (horizontal) où le texte commence à être affiché.

        y(int) : La position en pixels sur l'axe des ordonnées (vertical) où le texte commence à être affiché.

        maxi(int) : la position en x que le texte ne doit pas dépasser
        
        couleur(tuple): Une couleur définie sous forme de tuple (R, G, B) pour la couleur du texte.
    """
    mots = texte.split(' ')
    ligne_actuelle = ''
    y_offset = 0

    for mot in mots:
        # Vérifie si on peut ajouter le mot à la ligne actuelle
        if font.size(ligne_actuelle + mot)[0] <= screen_width - x - maxi:
            ligne_actuelle += mot + ' '
        else:
            # Dessine la ligne actuelle et réinitialise pour la nouvelle ligne
            screen.blit(font.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))
            ligne_actuelle = mot + ' '
            y_offset += font.get_height()  # Augmente l'offset pour la prochaine ligne

    # Dessine la dernière ligne si elle n'est pas vide
    if ligne_actuelle:
        screen.blit(font.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))