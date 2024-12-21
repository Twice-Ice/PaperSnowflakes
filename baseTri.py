import pygame
from pygame import Vector2
import numpy as np
from drawnSurface import DrawnSurface

class Tri:
    def __init__(self,
                 numOfTris : int = 12,
                 radius : int = 250,
                 pos : Vector2|tuple = (1900, 250),
                 circle : bool = True):
        self.rads = -np.radians(360/numOfTris)

        self.pos = Vector2(pos)
        self.diameter = 14
        self.radius = radius + self.diameter

        rawPoints = [Vector2(0,0),
                       Vector2(self.radius * np.cos(0), self.radius * np.sin(0)),
                       Vector2(self.radius * np.cos(self.rads), self.radius * np.sin(self.rads))]
        surfaceSize = Vector2(abs(rawPoints[1].x), abs(rawPoints[2].y))
        self.points = [point + Vector2(0, surfaceSize.y) + Vector2(0, 3) for point in rawPoints]
        
        self.surf = pygame.Surface(surfaceSize, pygame.SRCALPHA)
        self.surfaceInit(circle)
        self.paper = DrawnSurface(self.pos, surfaceSize)

    def surfaceInit(self,
                    circle : bool = True):
        """
            Initializes the base white surface of the triangle
        """
        self.surf.fill((255, 255, 255, 0))
        rect = self.surf.get_rect()
        color = (255, 255, 255, 255)

        if circle:
            pygame.draw.circle(self.surf, color, rect.bottomleft, self.radius)
            mask = pygame.Surface(self.surf.get_size(), pygame.SRCALPHA)
            mask.fill((255, 255, 255, 0))
            pygame.draw.polygon(mask, color, [
                rect.bottomleft,
                rect.bottomleft + Vector2(2 * self.radius * np.cos(0), 2 * self.radius * np.sin(0)),
                rect.bottomleft + Vector2(2 * self.radius * np.cos(self.rads), 2 * self.radius * np.sin(self.rads))
            ])
            mask = pygame.mask.from_surface(mask)
            mask = mask.to_surface(setcolor=(255, 255, 255, 255), unsetcolor=(0, 0, 0, 0))
            self.surf.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        else:
            pygame.draw.polygon(self.surf, color, self.points)

        # add a little fluff to prevent lines where the triangles don't line up perfectly on the full circle
        pygame.draw.line(self.surf, color, self.points[0], self.points[1], self.diameter)
        pygame.draw.line(self.surf, color, self.points[0], self.points[2], self.diameter)
        pygame.draw.circle(self.surf, color, self.points[0] + Vector2(self.diameter//2, -2), self.diameter//2)
    
    def undo(self):
        self.paper.undo()

    def redo(self):
        self.paper.redo()
        
    def draw(self,
             screen : pygame.Surface):
        screen.blit(self.surf, self.pos)

    def update(self,
               screen : pygame.Surface):
        self.draw(screen)
        self.paper.update(screen, pygame.mask.from_surface(self.surf))