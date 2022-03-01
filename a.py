from unicodedata import category
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
txt_size = 28
txt_font = pygame.font.Font(None, txt_size)
txt_font_2 = pygame.font.Font(None, txt_size-10)

rect_x = 100
rect_y = 100
rect_w = 150
rect_h = 35

category_list = ['Full Name', 'Email', 'Phone']
current_box = 0
input_boxes = []
for i in range(len(category_list)):
    input_boxes.append(pygame.Rect(rect_x, rect_y+(rect_h+30)*i, rect_w, rect_h))
text = ['']*len(category_list)

running = True
fps = 60
clock = pygame.time.Clock()

def draw_input_boxes():
    for i in range(len(input_boxes)):
        screen.blit(txt_font_2.render(category_list[i], True, (0, 0, 0)), (input_boxes[i].x+5, input_boxes[i].y-txt_size/2))
        pygame.draw.rect(screen, (255, 255, 255), input_boxes[i])
        if i == current_box:
            pygame.draw.rect(screen, (200, 0, 0), input_boxes[i], 2)
        else:
            pygame.draw.rect(screen, (0, 0, 0), input_boxes[i], 2)

        text_surface = txt_font.render(text[i], True, (0, 0, 0))
        screen.blit(text_surface, (input_boxes[i].x+5, input_boxes[i].y+10))
        
while running:
    screen.fill((207, 238, 250))
    clock.tick()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    draw_input_boxes()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if current_box != -1:
                if event.key == pygame.K_RETURN:
                    text[current_box] = ''
                elif event.key == pygame.K_BACKSPACE:
                    text[current_box] = text[current_box][:-1]
                else:
                    text[current_box] += event.unicode
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(input_boxes)):
                if input_boxes[i].collidepoint(mouse_x, mouse_y):
                    current_box = i
            
    pygame.display.flip()