import pygame
from pygame import Vector2
import globals as gb

class DrawnSurface:
    def __init__(self,
                 pos : Vector2|tuple = (0, 0),
                 size : Vector2|tuple = (gb.SX, gb.SY)):
        size = Vector2(size)
        size = Vector2(int(size.x), int(size.y))
        self.pos = pos
        self.surf = pygame.Surface(size, pygame.SRCALPHA)
        
        self.surf.fill((0, 0, 0, 0))
        self.mouse = Vector2(0,0)

        self.paintColor = (0, 0, 0, 255)

    def paint(self):
        oldMouse = self.mouse
        self.mouse = Vector2(pygame.mouse.get_pos())
        pressed = pygame.mouse.get_pressed(3)[0]
        
        if pressed:
            pygame.draw.line(self.surf, self.paintColor, oldMouse - self.pos, self.mouse - self.pos, 10)
            pygame.draw.circle(self.surf, self.paintColor, oldMouse - self.pos, 4)
            pygame.draw.circle(self.surf, self.paintColor, self.mouse - self.pos, 4)

    def draw(self,
             screen : pygame.Surface,
             mask : pygame.Mask):
        # self.surf.fill((255, 255, 255, 255))
        mask = mask.to_surface(setcolor=(0, 255, 0, 255), unsetcolor=(255, 0, 0, 0))
        self.surf.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)        
        screen.blit(self.surf, self.pos)

    def update(self,
               screen : pygame.Surface,
               mask : pygame.Mask):
        self.paint()
        self.draw(screen, mask)