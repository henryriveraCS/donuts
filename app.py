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
        self.A = 0
        self.B = 0
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
        while True:
            self.screen.fill((black))
            cosB, sinB = math.cos(self.B), math.sin(self.B)
            cosA, sinA = math.cos(self.A), math.sin(self.A)

            for T in range(0, 628, 40):
                cosT, sinT = math.cos(T/100), math.sin(T/100)

                x2 = self.r2 + self.r1 * cosT
                y2 = self.r1 * sinT
                for P in range(0, 628, 15):
                    cosP, sinP = math.cos(P/100), math.sin(P/100)

                    x = self.r1 * sinB * sinT + cosB * cosP * x2
                    y = -cosA * sinB * cosP * x2 + self.r1 * cosA * cosB * sinT - sinA * sinP * x2
                    self.draw(x, y)
            if self.A != 2:
                self.A += 0.001
                self.B += 0.0005
            else:
                self.A = 0
                self.B = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.update()

    def draw(self, x, y):
        """ Draws the donut """
        pygame.draw.circle(
                self.screen,
                white,
                (x+self.x_offset, y+self.y_offset),
                1
            )

class Screen():
    """ instance for initializing basic window stuff. """
    def __init__(self):
        self.font = pygame.font.SysFont(font, font_size)
        pygame.display.set_caption(window_title)
        self.screen = pygame.display.set_mode((window_height, window_width))
        #self.screen.fill(black)
        self.donut = Donut(self.screen) #updated when user clicks on screen

if __name__ == "__main__":
    pygame.init()
    screen = Screen()
    pygame.display.update()
    screen.donut.setup()
