# pygame-bootdev

# Asteroids Game

A classic arcade-style space shooter built with Pygame.

## Game Features

### Player Controls
- Rotate ship with arrow keys
- Thrust forward with UP key
- Fire bullets with SPACE

### Ship Physics
- Realistic momentum-based movement
- Gradual velocity decay
- Wrapping around screen edges

### Shooting Mechanics
- Bullets fire from ship's position
- Limited bullet lifespan
- Collision detection with asteroids

### Asteroid System
- Asteroids move across screen
- Screen edge wrapping
- Splitting mechanics:
  - Large asteroids split into medium ones
  - Medium asteroids split into small ones
  - Small asteroids are destroyed
  - Split asteroids move faster in opposite directions

## Built With
- Python
- Pygame
- Vector2 for physics calculations

## How to Play
1. Control your ship with arrow keys
2. Press SPACE to shoot
3. Destroy asteroids
4. Avoid collisions
