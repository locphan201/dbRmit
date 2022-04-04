import pygame as pg

def news_img():
    img = pg.image.load('Images\\hpNews\\thumbs.jpg')
    return img, img.get_rect()

def draw_homepage(window, scroll_y):
    img, img_rect = news_img()
    rect = pg.rect.Rect(0, scroll_y+100, img_rect.w, img_rect.h)
    pg.draw.rect(window, (0, 0, 0), rect, 4)
    window.blit(img, rect)

def draw_page(window, pages, active, scroll_y):
    if active == 0:
        draw_homepage(window, scroll_y)

    font = pg.font.SysFont('Arial', 20)
    pg.draw.rect(window, (150, 150, 150), (0, 0, 432, 50))
    txt = font.render(pages[active], True, (0, 0, 0))
    window.blit(txt, (20, 20))

def background(window):
    window.fill((207, 238, 250))

def customer_main(window):
    running = True
    clock = pg.time.Clock()
    fps = 60
    
    pages = ['Homepage', 'Products', 'Cart', 'Checkout', 'Order Confirmation']
    active = 0
    scroll_y = 0
    
    
    while running:
        clock.tick(fps)
        
        background(window)
        draw_page(window, pages, active, scroll_y)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4: scroll_y = min(scroll_y + 15, 0)
                if event.button == 5: scroll_y = max(scroll_y - 15, -768)

        pg.display.update()
    pg.quit()

def customer_init():
    pg.init()
    WIDTH, HEIGHT = 432, 768
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Nana\'s Bakery')
    customer_main(window)