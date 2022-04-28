import pygame as pg
from theme import *

items = []
add, sub = [], []

def sum():
    global items
    total = 0
    for i in range(len(items)):
        total += items[i][1] * items[i][2]
    return total

def modify(font, text, x, y, color=BLACK):
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(x, y))
    return txt, (rect.x, rect.y)

def add_item(name, price):
    global items, add, sub
    
    for i in range(len(items)):
        if items[i][0] == name:
            items[i][1] += 1
            return
    
    items.append([name, 1, price])
    sub.append(pg.Rect(235, 180+50*(len(items)-1), 10, 10))
    add.append(pg.Rect(275, 180+50*(len(items)-1), 10, 10))

def remove(index):
    global items, add, sub
    items.pop(index)
    add, sub = [], []
    for i in range(len(items)):
        sub.append(pg.Rect(235, 180+50*i, 10, 10))
        add.append(pg.Rect(275, 180+50*i, 10, 10))

def check_hit_button(x, y):
    global add, sub
    
    for i in range(len(add)):
        if add[i].collidepoint(x, y):
            items[i][1] += 1
            return 1, i
        
        if sub[i].collidepoint(x, y):
            items[i][1] -= 1
            if items[i][1] == 0:
                remove(i)
            return -1, i
    
    return 0, 1

def draw_cart(window):
    global items
    
    # Fonts
    item_font = pg.font.SysFont('Arial', 21)
    amount_font = pg.font.SysFont('Arial', 18)
    TAG = pg.font.SysFont('Arial', 22)

    window.blit(TAG.render("Item", True, BLACK), (30, 125))
    window.blit(TAG.render("Amount", True, BLACK), (225, 125))
    window.blit(TAG.render("Price", True, BLACK), (350, 125))
    pg.draw.line(window, BLACK, (0, 150), (500, 150), 2)

    for i in range(len(items)):
        window.blit(item_font.render(str(items[i][0]), True, BLACK), (30, 175+50*i))
        txt, pos = modify(amount_font, str(items[i][1]), 260, 185+50*i)
        window.blit(txt, pos)
        txt, pos = modify(amount_font, str(items[i][1]*items[i][2]), 375, 185+50*i)
        window.blit(txt, pos)
    
    for i in range(len(add)):
        pg.draw.rect(window, BLACK, add[i])
        txt, pos = modify(amount_font, "+", add[i].x+5, add[i].y+3, WHITE)
        window.blit(txt, pos)
        pg.draw.rect(window, BLACK, sub[i])
        txt, pos = modify(amount_font, "-", sub[i].x+5, sub[i].y+3, WHITE)
        window.blit(txt, pos)
    
    window.blit(item_font.render("Total", True, BLACK), (30, 175+50*(len(items)+1)))
    txt, pos = modify(amount_font, str(sum()), 375, 185+50*(len(items)+1))
    window.blit(txt, pos)