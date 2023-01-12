import pygame
import random

pygame.init()
# Used for random star location
star_x = 750
star_y = 600
screen_size = (800, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Constellation Maker")
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLUE = (0, 255, 255)
font = pygame.font.Font(None, 20)
stars = []

# Drawing Main Menu
def drawMain():
  # Make background black and give users instructions about how to use the program
    screen.fill(BLACK)
    text = font.render("(Click anywhere on the canvas to start making your own constellation)", True, WHITE)
    text2 = font.render("(Down arrow = Delete last star, Up arrow = Clear all stars, Left = Place a random star, Right = Create a random Constellation)", True, WHITE)
    screen.blit(text, [180, 25])
    screen.blit(text2, [5, 650])
    pygame.display.update()
    Star.main()

# Star class
class Star:
  def __init__(self, x, y, r, colour):
    self.x = x
    self.y = y
    self.r = r
    self.colour = colour

  def drawStars(self):
    pygame.draw.circle(screen, self.colour, (self.x, self.y), self.r)
    pygame.display.flip()
# Connect starOne and starTwo with a line
  def connectStars(starOne, starTwo):
    pygame.draw.line(screen, WHITE, (starOne.x, starOne.y), (starTwo.x, starTwo.y))
# Delete the last star added
  def deleteStar(stars):
    if len(stars) > 0:
       stars.pop()
    else:
# (Ensures that the program doesn't crash when it pops nothing)
       pass
# Generate a random star on the canvas
  def randomStar(stars):
    stars.append(Star((random.randint(0, star_x)),(random.randint(0, star_y)), 5, BLUE))
# Generate multiple random stars on the canvas to make them look like a constellation that may exist
  def randomConstellation(stars):
    for n in range(4, 12):
       stars.append(Star((random.randint(0, star_x)),(random.randint(0, star_y)), 5, BLUE))
    
# Clear the entire board of stars
  def clearStars(stars):
    stars.clear()
# Main Program 
  def main():
    done = False
    while not done:
      # Game set to True and will continue till it is set to False
      for event in pygame.event.get():                                       
        if event.type == pygame.QUIT:
            done = True
        # Append stars to list at user position
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            xMousePos = pos[0]
            yMousePos = pos[1]
            stars.append(Star(xMousePos, yMousePos, 4, BLUE))
        # Arrow key functions
        if event.type == pygame.KEYDOWN:
            # Undo last star added if down arrow key is pressed
            if event.key == pygame.K_DOWN:
                Star.deleteStar(stars)
                screen.fill(BLACK)
                pygame.display.flip()
            # Clear all stars from the canvas and update
            if event.key == pygame.K_UP:
                Star.clearStars(stars)
                screen.fill(BLACK)
                pygame.display.flip()
            # Add star to a random point on the canvas
            if event.key == pygame.K_LEFT:
                Star.randomStar(stars)
            # Generate a randomly made constellation
            if event.key == pygame.K_RIGHT:
                Star.randomConstellation(stars)

        # Drawing Stars and connect 
        for i in range(len(stars)):
          Star.drawStars(stars[i])
          if (len(stars) > 1 and i + 1 < len(stars)):
            Star.connectStars(stars[i], stars[i + 1])
    # Quit Constellation pygames
    pygame.quit()

drawMain()
