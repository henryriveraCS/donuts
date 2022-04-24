import sys
import math

import pygame

#pygame stuff
window_title = "donuts donuts donuts"
window_height = 600
window_width = 600
font = "Arial"
font_size = 25
depth = 0
vsync = 0
display = 0
flags = 0

#colors
white = (255, 255, 255)
black = (0, 0, 0)

class Donut():
    """ Donut class for rendering the object. """
    def __init__(self, screen):
        self.screen = screen
        self.enabled = False
        self.x_offset = window_width/2
        self.y_offset = window_height/2
        self.r1 = 40 #flat 2d circle
        self.r2 = 100 #distance from radius
    
    """ Rotates the axis to the specified axis position. """
    """
    def rotate(self):
        for T in range(0, 628, 15):
            cosT, sinT = math.cos(T/100), math.sin(T/100)
            pos_x2 = self.r2 + self.r1 * cosT
            pos_y2 = self.r1 + sinT
            for P in range(0, 628, 10):
                cosP, sinP = math.cos(P/100), math.sin(P/100)
                x = pos_x2*cosP
                y = pos_y2
                self.draw(x, y)
    """
    def setup(self):
        for T in range(0, 628, 15):
            cosT, sinT = math.cos(T/100), math.sin(T/100)

            x = self.r2 + self.r1 * cosT
            y = self.r1 * sinT
            self.draw(x, y)

    def draw(self, x, y):
        """ Draws the donut wherever pos_x and pos_y are set """
        pygame.draw.circle(
                self.screen,
                white,
                (x+self.x_offset, y+self.y_offset),
                1
            )
        pygame.display.update()

class Screen():
    """ instance for initializing basic window stuff. """
    def __init__(self):
        self.font = pygame.font.SysFont(font, font_size)
        pygame.display.set_caption(window_title)
        self.screen = pygame.display.set_mode((window_height, window_width))
        #self.screen.fill(black)
        self.donut = Donut(self.screen) #updated when user clicks on screen
        """
        self.screen = pygame.display.set_mode(
                size=(window_height, window_width),
                flags=flags,
                depth=depth
                )
        """

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
                print(pos_x, pos_y)
                #screen.donut.draw(pos_x, pos_y)
                screen.donut.setup()
                #screen.donut.rotate()
            if event.type == pygame.QUIT:
                pygame.quit()
