import pygame
from pygame import Vector2
from baseTri import Tri
import numpy as np
import math

class Snowflake:
    def __init__(self,
                 numOfTris : int = 12,
                 radius : int = 250,
                 snowflakePos : tuple|Vector2 = (500, 500),
                 trianglePos : tuple|Vector2 = (1000, 500)):
        self.triangle = Tri(numOfTris, radius, trianglePos)
        self.numOfTris = numOfTris
        self.offset = Vector2(snowflakePos)
        size = self.triangle.radius*2
        self.drawingSurface = pygame.Surface((size, size), pygame.SRCALPHA)
        self.drawingSurface.fill((255, 255, 255, 0))

    def draw(self,
             screen : pygame.Surface):
        drawingRect = self.drawingSurface.get_rect()
        drawingOffset = (drawingRect.width//2, drawingRect.height//2)

        mergedSurf = self.triangle.surf.copy()
        mergedSurf.blit(self.triangle.paper.surf, (0,0))
        rect = mergedSurf.get_rect()

        pivot = Vector2(rect.width//2, -rect.height//2)
        mirrorPivot = Vector2(rect.width//2, rect.height//2)

        for i in range(0, self.numOfTris, 2):
            angle = (360/self.numOfTris) * i
            rotatedSurface, newPos = self.pivotSurface(mergedSurf.copy(), pivot, angle)
            self.drawingSurface.blit(rotatedSurface, newPos + drawingOffset)
        
        for i in range(1, self.numOfTris, 2):
            angle = (360/self.numOfTris) * (i + 1)
            flippedSurface = pygame.transform.flip(mergedSurf.copy(), flip_x=False, flip_y=True)
            rotatedSurface, newPos = self.pivotSurface(flippedSurface, mirrorPivot, angle)
            self.drawingSurface.blit(rotatedSurface, newPos + drawingOffset)

        screen.blit(self.drawingSurface, self.offset - drawingOffset)

    def pivotSurface(self,
                  surface : pygame.Surface,
                  pivot : tuple|Vector2,
                  angle : float):
        pivot = Vector2(pivot)
        pivotPosition = pivot
        pivotPoint = pivotPosition - pivot
        rotatedSurface = pygame.transform.rotate(surface, angle)
        surfaceRect = rotatedSurface.get_rect()
        delta = pivotPosition - pivotPoint

        distance = math.hypot(delta.x, delta.y)
        originalAngle = math.atan2(delta.y, delta.x)
        rotatedDelta = Vector2(
            math.cos(originalAngle - math.radians(angle)) * distance,
            math.sin(originalAngle - math.radians(angle)) * distance
        )

        newPos = Vector2(
            pivotPoint.x + rotatedDelta.x - surfaceRect.width//2,
            pivotPoint.y + rotatedDelta.y - surfaceRect.height//2
        )

        return rotatedSurface, newPos
    
    def undo(self):
        self.triangle.undo()

    def redo(self):
        self.triangle.redo()

    def update(self,
               screen : pygame.Surface):
        self.triangle.update(screen)
        self.draw(screen)