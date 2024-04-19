# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
import random

WIDTH =  500
HEIGHT = 500

# Set up the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
print("Window set up!")

while running:

  # Did the user click the window close button?
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Fill the background with black
  screen.fill( (0,0,0) )
  pygame.draw.circle(screen, (255,0,255) , (200,200), 20)
  # Flip the display
  dt = clock.tick(30)
  pygame.display.flip()

# Done! Time to quit.
pygame.quit()
