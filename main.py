import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = updatable, drawable
Shot.containers = shots, updatable, drawable
Asteroid.containers = asteroids, updatable, drawable
AsteroidField.containers = updatable

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock() # Create a clock to control the frame rate
    dt = 0  # Initialize delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player instance at the center of the screen
    asteroid_field = AsteroidField()  # Create an asteroid field instance    


    while True:
        screen.fill("black")  # Fill the screen with black
        updatable.update(dt)

        # Collision detection: check if any asteroid collides with the player
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
            # Simple circle collision: distance between centers < sum of radii
            if (player.position - asteroid.position).length() < (player.radius + asteroid.radius):
                print("Game over!")
                pygame.quit()
                exit()

        for d in drawable:
            d.draw(screen)
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
