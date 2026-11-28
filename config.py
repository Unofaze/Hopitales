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

COULEUR_FOND = (0, 0, 0)  # Couleur du fond (noir)

def scale_fit(image, max_w, max_h):
    """Redimensionne une image en conservant son ratio pour tenir dans (max_w, max_h)."""
    img_w, img_h = image.get_size()
    if img_w <= 0 or img_h <= 0 or max_w <= 0 or max_h <= 0:
        return image
    ratio = min(max_w / img_w, max_h / img_h)
    new_w = max(1, round(img_w * ratio))
    new_h = max(1, round(img_h * ratio))
    return pygame.transform.scale(image, (new_w, new_h))


class File:
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        return self.valeurs == []

    def enfile(self, x):
        self.valeurs.insert(0, x)

    def defile(self):
        if self.est_vide():
            return None
        else:
            return self.valeurs.pop()

    def affiche(self):
        temp = File()
        chaine = ""

        while not self.est_vide():
            elem = self.defile()
            temp.enfile(elem)
            chaine = str(elem) + "|" + chaine

        while not temp.est_vide():
            self.enfile(temp.defile())

        print("|" + chaine)

def afficher_texte(texte, x, y, maxi, couleur, font=None):
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

        police (Font) : - (facultatif) la police a utiliser, creee par exemple avec pygame.font.SysFont("arial", 40)
                          ou pygame.font.Font("ma_police.ttf", 40).
                        - Si on ne la precise pas, une police par defaut est utilisee.
    """

    if font == None:
        font = pygame.font.SysFont("arial", 48)

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


# --------------------------------------------------------- |
# Infos comme ça qui peuvent servir (Joseph je vais te baiser à pas prendre des multiples de 1920 et 1080 pour les tailles des fichiers pixilart) :

    # coordonnées de la zone de texte des clients :
        # abscisse du message : 24/180 de la largeur de l'écran
        # largeur max du message : 59/180 de la largeur de l'écran
        # ordonnée du message : 22/109 de la hauteur de l'écran
        # hauteur max du message : 32/109 de la hauteur de l'écran

    # coordonnées du bouton "play" de l'écrand de démarrage :
        # abscisse du bouton : 3/100 de la largeur de l'écran
        # largeur du bouton : 32/100 de la largeur de l'écran
        # ordonnée du bouton : 15/100 de la hauteur de l'écran
        # hauteur du bouton : 11/100 de la hauteur de l'écran

    # coordonnées du sprite du client 1 :
        # abscisse du sprite du client 1 : 101/180 de la largeur de l'écran
        # largeur du sprite du client 1 : 63/180 de la largeur de l'écran
        # ordonnée du sprite du client 1 : 16/109 de la hauteur de l'écran
        # hauteur du sprite du client 1 : 93/109 de la hauteur de l'écran

    # coordonnées du sprite du client 2 :
        # abscisse du sprite du client 2 : 101/180 de la largeur de l'écran
        # largeur du sprite du client 2 : 42/180 de la largeur de l'écran
        # ordonnée du sprite du client 2 : 16/109 de la hauteur de l'écran
        # hauteur du sprite du client 2 : 84/109 de la hauteur de l'écran

    # coordonnées du sprite du client riche :
        # abscisse du sprite du client riche : 101/180 de la largeur de l'écran
        # largeur du sprite du client riche : 33/180 de la largeur de l'écran
        # ordonnée du sprite du client riche : 16/109 de la hauteur de l'écran
        # hauteur du sprite du client riche : 103/109 de la hauteur de l'écran    