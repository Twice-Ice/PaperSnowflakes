import os
import ctypes
# Step 1: Set DPI awareness to prevent Windows scaling
if os.name == "nt":  # Check if on Windows
    ctypes.windll.shcore.SetProcessDpiAwareness(2) 

import pygame
from pygame import Vector2
import globals as gb
from snowflake import Snowflake
from saveFile import File

screen = pygame.display.set_mode((gb.SX, gb.SY), pygame.NOFRAME)

doExit = False
clock = pygame.time.Clock()

snowflake : Snowflake = None
saveFile = None

def restart():
    global snowflake
    snowflake = Snowflake(12, 500)

restart()
while not doExit:
    dt = clock.tick(gb.FPS)/1000
    screen.fill(gb.BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        restart()
    if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
        saveFile = File()
        saveFile.saveFile()
        
        pygame.image.save(snowflake.drawingSurface, saveFile.filePath)

    snowflake.update(screen)

    pygame.display.flip()
pygame.quit()