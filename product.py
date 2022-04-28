import pygame as pg
import os
from theme import *

def product_imgs():
    items = []
    item_imgs = os.listdir('Resources\\Images\\Products')
    for img in item_imgs:
        image = pg.image.load('Resources\\Images\\Products\\' + img)
        image = pg.transform.scale(image, (100, 100))
        name = img.split('.')[0].replace('_', ' ').capitalize()
        items.append([name, image, 0, 0])
    return items

items = product_imgs()

def check_hit_product(scroll_y, x, y):
    global items
    for i in range(len(items)):
        if (30 < x and x < 402) and (scroll_y+150 + i*125 < y and y < scroll_y+250 + i*125):
            items[i][2] += 1
            return [items[i][0], items[i][2]*100]
    return []

def update_one(index, quantity):
    global items
    items[index][2] += quantity

def draw_product_page(window, scroll_y):
    global items
    
    font = pg.font.SysFont(font2, 28)
    
    for i in range(len(items)):
        window.blit(items[i][1], (30, scroll_y+150 + i*125))
        window.blit(font.render(items[i][0], True, BLACK), (165, scroll_y+175 + i*125))
        
        if items[i][2] > 0:
            pg.draw.circle(window, LIGHT_RED, (35, scroll_y+155 + i*125), 15)
            quantity = font.render(str(items[i][2]), True, WHITE)
            rect = quantity.get_rect(center=(35, scroll_y+155 + i*125))
            window.blit(quantity, (rect.x, rect.y))  