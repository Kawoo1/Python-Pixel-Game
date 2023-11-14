import pygame
import sys
import random

# Initialize Pygame library
pygame.init()

# ------------ Constants ------------
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

# Game variables
player_pos = [WIDTH // 2, HEIGHT // 2]
projectiles = []
enemies = []

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Game")
clock = pygame.time.Clock()
#----------------------------------------------------------------------------------------
# Draw section. A small group of functions to draw the game components.
# Draw the player
def draw_player():
    pygame.draw.circle(screen, WHITE, (int(player_pos[0]), int(player_pos[1])), 10)

# Draw projectiles
def draw_projectiles():
    for projectile in projectiles:
        pygame.draw.circle(screen, WHITE, (int(projectile[0]), int(projectile[1])), 5)

# Draw enemies
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, pygame.Rect(enemy[0], enemy[1], 10, 10))
#---------------------------------------------------------------------------------------
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left-click to shoot projectiles
            projectiles.append(list(player_pos))

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Enemy movement
    for enemy in enemies:
        enemy[0] += random.randint(-3, 3)
        enemy[1] += random.randint(-3, 3)

    # Spawn new enemies
    if len(enemies) < 10:
        enemies.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])

    # Check for collisions between projectiles and enemies
    for projectile in projectiles.copy():
        for enemy in enemies.copy():
            if pygame.Rect(enemy[0], enemy[1], 10, 10).colliderect(pygame.Rect(projectile[0], projectile[1], 5, 5)):
                enemies.remove(enemy)
                projectiles.remove(projectile)

    # Draw everything
    screen.fill((0, 0, 0))  #White background
    draw_player()           #Calling all the draw functions
    draw_projectiles()
    draw_enemies()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()