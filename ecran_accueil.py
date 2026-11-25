import config
import pygame

carte_width = config.screen_width * 4
carte_height = config.screen_height * 4
gameMap = pygame.Rect(0, 0, carte_width, carte_height)
gameMap.center = (config.screen_width // 2, config.screen_height // 2)

# Boutons des menus
def bouton_menus(x, y, width, height):
    """
    crée un bouton intéractif invisible de WIDTH et de HEIGHT donnée aux coordonnées données
    
    -------------
    Parametres :
    x(int) : position en abscisse du bouton
    y(int) : position en ordonnée du bouton
    width(int) : width du bouton
    height(int) : height du bouton

    Returns :
    res(bool) : True si le bouton est cliqué, False sinon
    
    Pré-conditions :
    toutes les variables doivent être des entiers positifs
    -------------
    """
    assert type(x) == int , "x n'est pas un entier"
    assert type(y) == int , "y n'est pas un entier"
    assert type(width) == int , "width n'est pas un entier"
    assert type(height) == int , "height n'est pas un entier"
    assert x > 0, "x n'est pas positif"
    assert y > 0, "y n'est pas positif"
    assert width > 0, "width n'est pas positive"
    assert height > 0, "height n'est pas positive"
    
    souris = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    bout = pygame.Rect(x, y, width, height)
    
    if bout.collidepoint(souris) and click[0] :
        return True
    return False

def draw():
    


