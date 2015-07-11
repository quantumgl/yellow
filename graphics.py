__author__ = 'user'

import pygame
import config
from maps import legends
pygame.init()
legends.init()

COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "PINK": (255, 127, 191)
}

soft_screen = pygame.Surface((160, 144))
player = pygame.Surface((14, 14))


def draw_logic_tile(tile_id, position):
    type_of_tile = legends.walkable_legend[tile_id%100]
    walkable_index_equivalent = legends.walkable_draws[type_of_tile]

    soft_screen.blit(legends.images[walkable_index_equivalent], position)

def draw_flavor_tile(tile_id, position):
    #type_of_tile = legends.drawable_legend[tile_id]

    if tile_id != -1:
        img = legends.images[tile_id]
        if not (img is None):
            soft_screen.blit(img, position)

def draw_logic_map(logic_map, player_position):
    for row in range(len(logic_map)):
        for column in range(len(logic_map[row])):
            draw_logic_tile(logic_map[row][column], ((player_position[0] + column -3)*16, (player_position[1] + row - 3)*16))

def draw_flavor_map(flavor_map, player_position):
    for row in range(len(flavor_map)):
        for column in range(len(flavor_map[row])):
            if not (flavor_map[row][column] is None):
                draw_flavor_tile(flavor_map[row][column], ((player_position[0] + column -3)*16, (player_position[1] + row - 3)*16))

def update_window(window):
    pygame.transform.scale(soft_screen, config.WINDOW_DIMENSIONS, window)