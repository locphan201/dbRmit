import pygame as pg
import os

COL = 2
IMG_SIZE = 175
SPACING = (432-IMG_SIZE*COL)/(COL+1)

def product_imgs():
    item_imgs = []
    items = os.listdir('Resources\\Images\\Products')
    for item in items:
        img = pg.image.load('Resources\\Images\\Products\\' + item)
        img = pg.transform.scale(img, (IMG_SIZE, IMG_SIZE))
        item_imgs.append(img)
    return item_imgs

def draw_product_page(window, scroll_y):
    img = product_imgs()
    
    row, col = 0, 0
    for i in range(len(img)):
        if col == COL:
            row += 1
            col = 0
        rect = pg.rect.Rect(SPACING + col*(IMG_SIZE+SPACING), scroll_y+100 + row*(IMG_SIZE+SPACING), IMG_SIZE, IMG_SIZE)
        pg.draw.rect(window, (0, 0, 0), rect, 4)
        window.blit(img[i], rect)
        col += 1