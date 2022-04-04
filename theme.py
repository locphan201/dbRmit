import pygame as pg

BACKGROUND = (207, 238, 250)
BUTTON = (0, 0, 0)
TAG = (0, 0, 0)
ERROR = (200, 0, 0)
HEADER = (150, 150, 150)

HEADER_FONT = pg.font.SysFont('Arial', 22)
HEADER_COLOR = (0, 0, 0)
FONT = pg.font.SysFont('Arial', 18)
FONT_COLOR = (0, 0, 0)

def convert(msg, header=False):
    if header:
        return HEADER_FONT.render(msg, True, HEADER_COLOR)
    else:
        return FONT.render(msg, True, FONT_COLOR)
