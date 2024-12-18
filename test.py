import pygame
import math
from pygame import Vector2

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotate Surface Around Arbitrary Point")

# Colors
WHITE = (255, 255, 255)

# Load or create a surface
surface = pygame.Surface((100, 50), pygame.SRCALPHA)
surface.fill((255, 0, 0))

# Arbitrary pivot point in world space
pivot_point = (pygame.math.Vector2(350, 250) - Vector2(50, -25))

# Surface's initial position in world space (top-left corner)
surface_position = [350, 250]  # Adjust as needed

# Rotation angle
angle = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Increment the rotation angle
    angle += 1

    # Calculate the rotated surface
    rotated_surface = pygame.transform.rotate(surface, angle)

    # Calculate the offset for the new position of the rotated surface
    surface_rect = rotated_surface.get_rect()
    dx = surface_position[0] - pivot_point[0]
    dy = surface_position[1] - pivot_point[1]

    # Rotate the offset around the pivot point
    distance = math.hypot(dx, dy)
    original_angle = math.atan2(dy, dx)
    rotated_dx = math.cos(original_angle - math.radians(angle)) * distance
    rotated_dy = math.sin(original_angle - math.radians(angle)) * distance

    # Compute the new top-left position of the rotated surface
    new_position = (
        pivot_point[0] + rotated_dx - surface_rect.width // 2,
        pivot_point[1] + rotated_dy - surface_rect.height // 2
    )

    # Draw the rotated surface
    screen.blit(rotated_surface, new_position)

    # Draw the pivot point for visualization
    pygame.draw.circle(screen, (255, 0, 0), new_position, 3)
    pygame.draw.circle(screen, (0, 0, 255), pivot_point, 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
