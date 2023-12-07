import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

game_images = dict()
game_images['player'] = pygame.image.load('./sprites/bowser.png').convert_alpha()

sprite_width = 32
sprite_height = 32
num_sprites = game_images['player'].get_width() // sprite_width

# List to store all sprites
sprites = []
for i in range(num_sprites):
    sprite_x = i * sprite_width
    sprite = game_images['player'].subsurface(pygame.Rect((sprite_x, 0, sprite_width, sprite_height)))
    sprites.append(sprite)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Initial frame set to middle frame when idle. Subtract 3 to move 3 images left.
frame_idle = (num_sprites // 2) - 6
frame = frame_idle
frame_delta = 0

running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()
    flip_sprite = False  # Flag to indicate if sprite should be flipped

    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        flip_sprite = False
        frame = 0  # First frame for moving up - DOES WORK
    elif keys[pygame.K_s]:
        player_pos.y += 300 * dt
        flip_sprite = True
        frame = 10  # First frame for moving down - DOESNT WORK
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        flip_sprite = True  # Set flag to True
        frame_delta = 1
        frame = min(frame + frame_delta, num_sprites - 4)  # Cycle forward in sprite images, regardless of direction
    elif keys[pygame.K_d]:
        player_pos.x += 300 * dt
        flip_sprite = False  # Set flag to False
        frame_delta = 1
        frame = min(frame + frame_delta, num_sprites - 4)  # Cycle forward
    else:
        frame_delta = 0
        frame = frame_idle

    sprite_to_blit = sprites[frame]  # Get sprite
    if flip_sprite:
        sprite_to_blit = pygame.transform.flip(sprite_to_blit, True, False)  # Flip the sprite

    screen.blit(sprite_to_blit, player_pos)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
