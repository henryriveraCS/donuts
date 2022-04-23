import sys
import math

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
donut_size = 100

#colors
white = (255, 255, 255)
black = (0, 0, 0)
class Donut():
    """ Donut class for rendering the object. """
    def __init__(self, screen):
        self.screen = screen
        self.enabled = False
        self.size = 0
        self.pos_x = 0
        self.pos_y = 0
        self.axis = 0
        self.r1 = 40 #flat 2d circle
        self.r2 = 100 #distance from radius
    
    def rotate(self):
        """ Rotates the axis to the specified axis position. """
        for T in range(0, 628, 15):
            cosT, sinT = math.cos(T/100), math.sin(T/100)
            self.pos_x = self.r2 + (self.r1*cosT)
            self.pos_y = self.r1 + sinT
            self.draw(self.size, self.pos_x, self.pos_y)
        print("donut rotating.")

    def draw(self, size, pos_x, pos_y):
        """ Draws the donut wherever pos_x and pos_y are set """
        self.size = size
        self.pos_x = pos_x
        self.pos_y = pos_y
        pygame.draw.circle(self.screen, white, (self.pos_x, self.pos_y), 1)

class Screen():
    """ instance for initializing basic window stuff. """
    def __init__(self):
        self.font = pygame.font.SysFont(font, font_size)
        pygame.display.set_caption(window_title)
        self.screen = pygame.display.set_mode(
                size=(window_height, window_width),
                flags=flags,
                depth=depth
                )
        self.screen.fill(black)
        self.donut = Donut(self.screen) #updated when user clicks on screen

    def load_donut(self, pos_x, pos_y):
        """ Loads donut wherever user clicks on the screen. """
        self.donut.draw(pos_x, pos_y)

if __name__ == "__main__":
    pygame.init()
    screen = Screen()
    pygame.display.update()
    while True:
        ev = pygame.event.get()
        for event in ev:
            #place donuts wherever user clicks
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                screen.donut.draw(donut_size, pos_x, pos_y)
                screen.donut.rotate()
            if event.type == pygame.QUIT:
                pygame.quit()
