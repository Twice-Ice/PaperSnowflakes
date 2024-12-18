import pygame
from pygame import Vector2
import numpy as np
from drawnSurface import DrawnSurface

class Tri:
    def __init__(self,
                 numOfTris : int = 12,
                 radius : int = 250,
                 pos : Vector2|tuple = (1900, 250)):
        self.pos = Vector2(pos)
        rads = -np.radians((360/numOfTris)*1.02)
        rawPoints = [Vector2(0,0),
                       Vector2(radius * np.cos(0), radius * np.sin(0)),
                       Vector2(radius * np.cos(rads), radius * np.sin(rads))]

        surfaceSize = Vector2(abs(rawPoints[1].x), abs(rawPoints[2].y))
        
        self.points = [point + Vector2(0, surfaceSize.y) for point in rawPoints]

        self.surf = pygame.Surface(surfaceSize, pygame.SRCALPHA)
        self.surf.fill((255, 255, 255, 0))
        pygame.draw.polygon(self.surf, (255, 255, 255, 255), self.points)

        self.paper = DrawnSurface(self.pos, surfaceSize)
        
    def draw(self,
             screen : pygame.Surface):
        screen.blit(self.surf, self.pos)
        # pygame.draw.polygon(screen, (255, 0, 0), [point + self.pos for point in self.points])

    def update(self,
               screen : pygame.Surface):
        self.draw(screen)
        self.paper.update(screen, pygame.mask.from_surface(self.surf))