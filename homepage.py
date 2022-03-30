import pygame as pg
from theme import *

def get_open_time():
    return ['Time: ', '8am - 9pm ', 'from Monday to Saturday']

def get_location():
    location = ['Location: ']
    location.append('123 Ly Thuong Kiet')
    location.append('A District, Ho Chi Minh city')
    return location

def get_contact():
    contact = ['Contact us: ', ]
    contact.append('Phone number: 012345678')
    contact.append('Email: Nanabakery@gmail.com')
    return contact

def draw_homepage(window):
    # Set fonts
    title = pg.font.Font(font2, 25)
    header = pg.font.Font(font3, 25)
    paragraph =  pg.font.Font(font2, 20)
    
    # Setup texts
    best_seller = header.render('Best seller of the week:', True, BLACK)
    seasonal_product = header.render('Seasonal product:', True, BLACK)
    welcome = title.render('Welcome to Nana\'s Bakery', True, BLACK)
    slogan = paragraph.render('Bake with love', True, BLACK)
    time = get_open_time()
    location = get_location()
    contact  = get_contact()

    # Load and resize image
    cake_img = pg.image.load('Resources\\Images\\Homepage\\thumb0.jpg')
    cake_img = pg.transform.scale(cake_img, (150,150))
    
    # Welcome and Infomation
    pg.draw.rect(window,PINK,(0,100,432,150))
    window.blit(cake_img, (0, 100))
    window.blit(welcome, (160,100))
    window.blit(slogan, (230, 130))
    
    for i in range(len(time)):
        if i == 0:
            window.blit(paragraph.render(time[i], True, BLACK), (180, 160))
        else:
            window.blit(paragraph.render(time[i], True, BLACK), (230, 160+(i-1)*20))
    
    for i in range(len(location)):
        if i == 0:
            window.blit(paragraph.render(location[i], True, BLACK), (150, 200))
        else:
            window.blit(paragraph.render(location[i], True, BLACK), (220, 200+(i-1)*20))  
    
    # Recomendation
    window.blit(best_seller, (0, 250))
    window.blit(seasonal_product, (0,500))
    
    # Contact us
    pg.draw.rect(window,PINK,(0,700,432,70))
    for i in range(len(contact)):
        window.blit(paragraph.render(contact[i], True, BLACK), (0, 700+i*25))