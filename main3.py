import pygame
pygame.init()

# Screen setup
screenwidth, screenheight = 500, 500
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Color Changing")

# Define colors
colors = {
    "red": pygame.Color("red"),
    "green": pygame.Color("green"),
    "blue": pygame.Color("blue"),
    "yellow": pygame.Color("yellow"),
    "white": pygame.Color("white")
}

# Sprite setup
current_color = colors["white"]
x, y = 30, 30
spritewidth, spriteheight = 60, 60
clock = pygame.time.Clock()

done = False
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Key presses (outside event loop)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3

    # Keep sprite inside screen
    x = min(max(0, x), screenwidth - spritewidth)
    y = min(max(0, y), screenheight - spriteheight)

    # Change color based on position
    if x == 0:
        current_color = colors["red"]
    elif x == screenwidth - spritewidth:
        current_color = colors["blue"]
    elif y == 0:
        current_color = colors["green"]
    elif y == screenheight - spriteheight:
        current_color = colors["yellow"]
    else:
        current_color = colors["white"]

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, current_color, (x, y, spritewidth, spriteheight))
    pygame.display.flip()
    clock.tick(90)

pygame.quit()