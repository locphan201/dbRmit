import pygame as pg
from homepage import *
from product import *
from cart import *
from order import *
from about_us import *
from db_connector import *
from theme import *

USER_INFO = []
ORDER_UPDATE = False

def user_information(account):
    global USER_INFO
    USER_INFO = get_user_info(account)

def draw_page(window, pages, active, scroll_y, back, nxt):
    global ORDER_UPDATE
    INDENT = 55
    
    if active == 0:
        draw_homepage(window)
        scroll_y = 0
    elif active == 1:
        draw_product_page(window, scroll_y)
    elif active == 2:
        draw_cart(window)
    elif active == 3:
        if not ORDER_UPDATE:
            ORDER_UPDATE = True
            get_order(USER_INFO[0])
        draw_order_page(window)
    elif active == 4:
        scroll_y = draw_about_us(window, scroll_y)

    pg.draw.rect(window, LIGHT_RED, (0, 0, 432, 65))
    pg.draw.rect(window, GREY, (0, 65, 432, 35))
    h_font = pg.font.Font(font1,50)
    header = h_font.render('Nana\'s Bakery', True, BLACK)
    window.blit(header, (100,0))
    
    font = pg.font.SysFont('Arial', 20)
    #Previous page
    if active >= 1:
        txt = font.render(pages[active-1], True, (50, 50, 50))
        back = txt.get_rect(center=(40, 25))
        back = pg.Rect(INDENT, 70, back.w, back.h)
        window.blit(txt, (INDENT, 70))

    #Current page
    txt = font.render(pages[active], True, (0, 0, 0))
    window.blit(txt, (INDENT+125, 70))

    #Next page
    if active < len(pages)-1:
        txt = font.render(pages[active+1], True, (50, 50, 50))
        nxt = txt.get_rect(center=(40, 25))
        nxt = pg.Rect(INDENT+250, 70, nxt.w, nxt.h)
        window.blit(txt, (INDENT+250, 70))

    return back, nxt, scroll_y

def background(window):
    window.fill(BACKGROUND)

def customer_main(window):
    running = True
    clock = pg.time.Clock()
    fps = 60
    back, nxt = pg.Rect(40, 0, 100, 50), pg.Rect(290, 0, 100, 50)
    pages = ['Homepage', 'Products', 'Cart', 'Order', 'About us']
    active = 0
    scroll_y = 0
    
    while running:
        clock.tick(fps)
        
        background(window)
        back, nxt, scroll_y = draw_page(window, pages, active, scroll_y, back, nxt)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if active == 0:
                    if check_event_homepage(event.pos[0], event.pos[1]):
                        active = 1
                
                elif active == 1:
                    if event.button == 1:
                        item = check_hit_product(scroll_y, event.pos[0], event.pos[1])
                        if item != []:    
                            add_item(item[0], item[1])
                    if event.button == 4: scroll_y = min(scroll_y + 15, 0)
                    if event.button == 5: scroll_y = max(scroll_y - 15, -768)
                
                elif active == 2:
                    button, i = check_hit_button(event.pos[0], event.pos[1])
                    if button == -1:
                        update_one(i, -1)
                    elif button == 1:
                        update_one(i, 1)
                    elif button == 2:
                        cart_checkout(get_items(), USER_INFO[0])
                        remove_all()
                
                elif active == 3:
                    check_order_events(event.pos[0], event.pos[1])
                
                if event.button == 1:
                    if back.collidepoint(event.pos):
                        active = max(active - 1, 0)
                        scroll_y = 0
                    if nxt.collidepoint(event.pos):
                        active = min(active + 1, len(pages)-1)
                        scroll_y = 0
        pg.display.update()   
        
    pg.quit()

def customer_init(info):
    pg.init()
    user_information(7534872145)
    WIDTH, HEIGHT = 432, 768
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Nana\'s Bakery')
    customer_main(window)