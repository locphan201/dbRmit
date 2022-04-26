import pygame as pg
from theme import *

pg.init()

# Fonts
item_font = pg.font.SysFont('Arial', 21)
amount_font = pg.font.SysFont('Arial', 18)
type_font = pg.font.SysFont(font3, 20)

subtract_symbol = item_font.render('-', True, WHITE)
add_symbol = item_font.render('+', True, WHITE)

# Dictionaries
temp_item_order = {"Red Velvet Cake": 0, "Carrot Cake": 0, "Sponge Cake": 0, "Fruit Cake": 0, "Salted Eggs Cake": 0}
item_price = {"Red Velvet Cake": 100000, "Carrot Cake": 30000, "Sponge Cake": 55000, "Fruit Cake": 65000,
              "Salted Eggs Cake": 25000}
subtract_click_pos = {}
add_click_pos = {}

def draw_cart(window):
    item_starting_pos_y = 150

    window.blit(type_font.render("Item", True, BLACK), (65, 170))
    window.blit(type_font.render("Amount", True, BLACK), (235, 170))
    window.blit(type_font.render("Price", True, BLACK), (360, 170))

    for cart_item in temp_item_order:
        item_starting_pos_y += 50

        if temp_item_order[cart_item] >= 0:
            continue
        else:
            temp_item_order[cart_item] = 0

        window.blit(item_font.render(cart_item, True, BLACK), (30, item_starting_pos_y))

        # Print amount of item in cart
        window.blit(amount_font.render(str(temp_item_order[cart_item]), True, BLACK),(248, item_starting_pos_y))
            # Print price
        window.blit(amount_font.render(str(temp_item_order[cart_item] * item_price[cart_item]), True, BLACK),(350, item_starting_pos_y))