import pygame
import random
 
# Colors
Black = (0, 0, 0)
White = (255, 255, 255)
 
Screen_Height = 800
Screen_Width = 600
BALL_SIZE = 20
# Random Color for ball each time game launches
Ball_Color = (random.randrange(255), random.randrange(255), random.randrange(255))
 
class Ball:
    # Ball Class
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x2 = 0
        self.y2 = 0
 
def make_ball():
    # Creating a new ball
    ball = Ball()
    # Starting location of where the ball will spawn
    ball.x = random.randrange(BALL_SIZE, Screen_Height)
    ball.y = random.randrange(BALL_SIZE, Screen_Width)
 
    # Speed speed of the ball
    ball.x2 = random.randrange(-5, 8)
    ball.y2 = random.randrange(-5, 8)
 
    return ball
 
 
def main():
    # Init all modules
    pygame.init()
 
    # Set the height and width of the screen
    size = [Screen_Height, Screen_Width]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Bouncing Balls")
 
    # Loop until the user clicks the close button.
    done = False
 
    clock = pygame.time.Clock()
 
    ball_list = []
    ball = make_ball()
    ball_list.append(ball)
 
    # Main loop
    while not done:
        # Key features
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space to spawn a new ball
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)
                # Up arrow key clears all balls
                if event.key == pygame.K_UP:
                    ball_list.clear()
                    pygame.display.flip()
                # Down arrow key removes the last ball added
                if event.key == pygame.K_DOWN:
                    if len (ball_list) > 0:          
                     ball_list.pop()
                else: 
                    pass
                # Right arrow key to speed up ball
                if event.key == pygame.K_RIGHT:
                    ball.x2 = ball.x2*2
                    ball.y2 = ball.y2*2
                # Left arrow key slows down the ball
                if event.key == pygame.K_LEFT:
                    ball.x2 = ball.x2/2
                    ball.y2 = ball.y2/2

        # Ball movement
        for ball in ball_list:
            ball.x += ball.x2
            ball.y += ball.y2
 
            # Bounce the ball if needed
            if ball.y > Screen_Width - BALL_SIZE or ball.y < BALL_SIZE:
                ball.y2 *= -1
            if ball.x > Screen_Height - BALL_SIZE or ball.x < BALL_SIZE:
                ball.x2 *= -1
 
        # Set the screen background color
        screen.fill(Black)
 
        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, Ball_Color, [ball.x, ball.y], BALL_SIZE)
 
        clock.tick(60)
 
        # Update the screen to show the balls drawn
        pygame.display.flip()

    pygame.quit()
 
main()
