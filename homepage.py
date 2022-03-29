import pygame as pg

def news_img():
    img = pg.image.load('Images\\hpNews\\thumbs.jpg')
    return img, img.get_rect()

def draw_homepage(window, scroll_y):
    img, img_rect = news_img()
    rect = pg.rect.Rect(0, scroll_y+100, img_rect.w, img_rect.h)
    pg.draw.rect(window, (0, 0, 0), rect, 4)
    window.blit(img, rect)