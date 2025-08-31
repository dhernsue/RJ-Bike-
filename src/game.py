def start_game():
    print("Welcome to Bike Racing Game!")
    print("Choose your bike and start racing... 🏁")
import pygame
import sys

# Pygame initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RJ Bike Racing 🚴‍♂️")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Bike setup (rectangle demo)
bike = pygame.Rect(WIDTH//2 - 25, HEIGHT-100, 50, 80)

# Main Game Loop
running = True
while running:
    screen.fill(WHITE)

    # Event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key Press (Bike Move)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bike.x > 0:
        bike.x -= 5
    if keys[pygame.K_RIGHT] and bike.x < WIDTH-50:
        bike.x += 5

    # Draw Bike
    pygame.draw.rect(screen, RED, bike)

    # Update
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
