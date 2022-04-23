import sys

import pygame

#pygame stuff
window_title = "donuts donuts donuts"
window_height = 640
window_width = 480
font = "Arial"
font_size = 25
depth = 0
vsync = 0
display = 0
flags = 0

#colors
white = (255, 255, 255)
black = (0, 0, 0)

class Screen():
    def __init__(self):
        self.font = pygame.font.SysFont(font, font_size)
        pygame.display.set_caption(window_title)
        self.screen = pygame.display.set_mode(
                size=(window_height, window_width),
                flags=flags,
                depth=depth
                )
        self.screen.fill(black)






if __name__ == "__main__":
    pygame.init()
    screen = Screen()
    pygame.display.update()
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                print(pos_x, pos_y)
            if event.type == pygame.QUIT:
                pygame.quit()
