from tkinter import UNDERLINE
import pygame as pg
from theme import *

USER_INFO = []

def get_info(info):
    global USER_INFO
    USER_INFO = info

def draw_personal_info(window):
    global USER_INFO
    font = pg.font.SysFont('Arial', 20)
    
    for i in range(len(USER_INFO)):
        txt = font.render(USER_INFO[i], True, (0, 0, 0))
        window.blit(txt, (30, i*50+150))