import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 866, 677
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("❤️ heart animiation ")

clock = pygame.time.Clock()

def draw_heart(surface, x_offset, y_offset, scale, color):
    points = []
    
    # Heart equation
    for t in range(0, 360):
        t = math.radians(t)
        
        x = 16 * math.sin(t)**3
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) 
              - 2 * math.cos(3*t) - math.cos(4*t))
        
        # Scale and move
        x = x * scale + x_offset
        y = y * scale + y_offset
        
        points.append((x, y))
    
    pygame.draw.polygon(surface, color, points)

# Animation variables
scale = 15
scale_direction = 1

while True:
    screen.fill((0, 0, 0))  # Black background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pulsing animation
    scale += 0.1 * scale_direction
    if scale > 18 or scale < 14:
        scale_direction *= -1

    # Draw heart
    draw_heart(screen, WIDTH // 2, HEIGHT // 2, scale, (255, 0, 100))

    pygame.display.flip()
    clock.tick(60)