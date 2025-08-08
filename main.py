import pygame
from constants import *
from circleshape import CircleShape
from player import Player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = updatable, drawable

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock() # Create a clock to control the frame rate
    dt = 0  # Initialize delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player instance at the center of the screen


    while True:
        screen.fill("black")  # Fill the screen with black
        player.update(dt)  # Update the player
        player.draw(screen)  # Draw the player
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000.0  # Calculate delta time in seconds
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
