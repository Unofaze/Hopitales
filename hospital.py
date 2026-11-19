import config
import pygame


def createRoom(x, y, w, l):    # (room_abscissa, room_ordinate, room_width, room_length)
    return pygame.Rect(x, y, w, l)


waitingRoom = createRoom(0, 0, 300, 300)
waitingRoom.center = (config.screen_width//2, config.screen_height//2)


def draw():
    roomDisplayed = waitingRoom.move(config.camera_x, config.camera_y)
    pygame.draw.rect(config.screen, (200, 200, 200), roomDisplayed)