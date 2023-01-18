import pygame
import random

pygame.init()

# Color Properties and Screen size
BLACK = [0, 0, 0]
WHITE = [255,255,255]
Screen_Size = [900, 700]
 
# Title 
screen = pygame.display.set_mode(Screen_Size)
pygame.display.set_caption("Snow Fall Simulator")

# Empty Snow Array
Snow = []

# Loop Snow Fall
for i in range(500):
    x = random.randrange(0, 900)
    y = random.randrange(0, 900)
    Snow.append([x, y])

# Set Timer for Snow Flake falls
timer = pygame.time.Clock()
done = False
while not done:

    for event in pygame.event.get(): 
        # Click X to exit the program
        if event.type == pygame.QUIT: 
            done = True
    # Fill background color to black
    screen.fill(BLACK)
    for i in range(len(Snow)):
        # Draw the snow that is falling
        pygame.draw.circle(screen, WHITE, Snow[i], 1.1)
 
        Snow[i][1] += random.randint(0, 10)
        # Move Snow back to top to a new random position
        if Snow[i][1] > 900:
            y = random.randrange(-50, -10)
            Snow[i][1] = y
            x = random.randrange(0, 900)
            Snow[i][0] = x
 
    pygame.display.update()
    timer.tick(200)
pygame.quit()
