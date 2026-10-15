print("skibidi world")
import pygame

pygame.init()

# Set up the window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()
running = True

# --- 1. NEW: Player Setup ---
player_size = 40
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 5
player_color = (255, 50, 50)  # Red

# The game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- 2. NEW: Player Movement ---
    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Optional: Keep the player inside the screen boundaries
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # --- Rendering ---
    screen.fill((30, 30, 60))  # Background colour

    # --- 3. NEW: Draw the Player ---
    # pygame.draw.rect(surface, color, (x, y, width, height))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

pygame.quit()