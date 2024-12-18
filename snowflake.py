import pygame
from pygame import Vector2
from baseTri import Tri
import numpy as np
import math

class Snowflake:
    def __init__(self,
                 numOfTris : int = 12,
                 radius : int = 250,
                 snowflakeOffset : tuple|Vector2 = (500, 500),
                 triangleOffset : tuple|Vector2 = (1000, 500)):
        self.triangle = Tri(numOfTris, radius, triangleOffset)
        self.numOfTris = numOfTris
        self.offset = Vector2(snowflakeOffset)

    def draw(self,
             screen : pygame.Surface):
        mergedSurf = self.triangle.surf.copy()
        mergedSurf.blit(self.triangle.paper.surf, (0,0))
        rect = mergedSurf.get_rect()

        for i in range(0, self.numOfTris, 2):
            angle = (360/self.numOfTris) * i
            rotatedSurface, newPos = self.pivotSurface(mergedSurf.copy(), (rect.width//2, -rect.height//2), angle)
            screen.blit(rotatedSurface, newPos + self.offset)
        
        for i in range(1, self.numOfTris, 2):
            angle = (360/self.numOfTris) * (i + 1)
            flippedSurface = pygame.transform.flip(mergedSurf.copy(), flip_x=False, flip_y=True)
            rotatedSurface, newPos = self.pivotSurface(flippedSurface, (rect.width//2, rect.height//2), angle)
            screen.blit(rotatedSurface, newPos + self.offset)

            # if i == 0:
            #     ogTrianglePos = self.triangle.pos + Vector2(rect.width//2, rect.height//2)
            #     pivPos = self.triangle.pos + Vector2(0, rect.height) + Vector2(
            #         np.cos(np.radians(-(360/self.numOfTris)/2)) * 250,
            #         np.sin(np.radians(-(360/self.numOfTris)/2)) * 250
            #     )
            #     pygame.draw.circle(screen, (255, 0, 0), pivPos, 5)
            #     pygame.draw.circle(screen, (0, 255, 255), ogTrianglePos, 5)
            # pygame.draw.circle(screen, (255, 0, 0), newPos + Vector2(500, 500), 2)
            # pygame.draw.circle(screen, (0, 0, 255), pivotPoint + Vector2(500, 500), 5)
            # pygame.draw.circle(screen, (0, 255, 255), Vector2(500, 500), 5)

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

    def update(self,
               screen : pygame.Surface):
        self.triangle.update(screen)
        self.draw(screen)