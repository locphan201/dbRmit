import pygame as pg
from db_connector import *
from theme import *

ORDER_INFO = []

def show(window, font, text, x, y, color=BLACK):
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(x, y))
    window.blit(txt, (rect.x, rect.y))

def draw_order_page(window):
    global ORDER_INFO
    
    font = pg.font.SysFont(font2, 28)
    show(window, font, 'Order Information', 216, 125)
    show(window, font, 'Order ID', 216, 125)
    