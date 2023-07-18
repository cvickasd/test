import pygame

class Hero:
    def __init__(self, size:int, color:int, win:int, width:int, height:int):
        self.size = size
        self.win = win
        self.color = color

        self.width = width
        self.height = height

    def update(self):
        pygame.draw.rect(self.win, self.color, [self.win[0]/2+self.width,self.win[1]/2+self.height])