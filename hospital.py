import config
import game_map
import pygame

# (x, y, largeur, hauteur) dans le repère monde
waiting_room = (-150, -150, 300, 300)

def build()
    if 

def draw():
    x, y, largeur, hauteur = waiting_room
    room_displayed = game_map.monde_vers_ecran_rect(x, y, largeur, hauteur)
    pygame.draw.rect(config.screen, (200, 200, 200), room_displayed)