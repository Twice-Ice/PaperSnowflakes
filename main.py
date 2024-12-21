import os
import ctypes
# Step 1: Set DPI awareness to prevent Windows scaling
if os.name == "nt":  # Check if on Windows
    ctypes.windll.shcore.SetProcessDpiAwareness(2) 

import pygame
import globals as gb
from snowflake import Snowflake
from saveFile import File
from drawnSurface import DrawnSurface

screen = pygame.display.set_mode((gb.SX, gb.SY), pygame.NOFRAME)

doExit = False
clock = pygame.time.Clock()

snowflake : Snowflake = None
saveFile = None
cooldown = 0

def startGame():
    global snowflake
    snowflake = Snowflake(12, 500, snowflakePos=(750, gb.SY//2), trianglePos=(1250, gb.SY//2), circle=True)

startGame()
while not doExit:
    dt = clock.tick(gb.FPS)/1000
    cooldown -= dt
    screen.fill(gb.BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    keys = pygame.key.get_pressed()
    if cooldown <= 0:
        if keys[pygame.K_r]:
            startGame()
            cooldown = .1
        if keys[pygame.K_LCTRL]:
            if keys[pygame.K_LSHIFT]:
                if keys[pygame.K_s]:
                    if saveFile == None:
                        saveFile = File()
                        saveFile.saveFile()
                    pygame.image.save(snowflake.drawingSurface, saveFile.filePath)

                if keys[pygame.K_z]:
                    cooldown = .15
                    snowflake.redo()
            else:
                if keys[pygame.K_s]:
                    saveFile = File()
                    saveFile.saveFile()
                    pygame.image.save(snowflake.drawingSurface, saveFile.filePath)

                if keys[pygame.K_z]:
                    cooldown = .15
                    snowflake.undo()

    snowflake.update(screen)

    pygame.display.flip()
pygame.quit()