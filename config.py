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

