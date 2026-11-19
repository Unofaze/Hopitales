import config
import pygame

map_width = config.screen_width * 4
map_height = config.screen_height * 4
gameMap = pygame.Rect(0, 0, map_width, map_height)
gameMap.center = (config.screen_width // 2, config.screen_height // 2)


TAILLE_CASE = 100

def draw():
    rectDisplayed = gameMap.move(config.camera_x, config.camera_y)
    pygame.draw.rect(config.screen, (105, 176, 47), rectDisplayed)
    
    for x in range(rectDisplayed.left, rectDisplayed.right + 1, TAILLE_CASE):
        pygame.draw.line(
            config.screen,
            (255, 0, 0),
            (x, rectDisplayed.top),
            (x, rectDisplayed.bottom),
            2,
        )

    for y in range(rectDisplayed.top, rectDisplayed.bottom + 1, TAILLE_CASE):
        pygame.draw.line(
            config.screen,
            (255, 0, 0),
            (rectDisplayed.left, y),
            (rectDisplayed.right, y),
            2,
        )
