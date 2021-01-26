import sys
import os
import pygame

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
FRAME_RATE = 40

BLACK = (0, 0, 0)

# Main loop
def main():
    for event in pygame.event.get():
        handle_event(event)

    update()
    draw()
    clock.tick(FRAME_RATE)  # Pause the clock to maintain 40 frames per second


"""
EVENTS section - how the code reacts when users do things
"""
def handle_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


"""
UPDATE section - manipulate everything on the screen
"""
def update():
    pass


"""
DRAW section - make everything show up on screen
"""
def draw():
    screen.fill(BLACK)  # Fill the screen with one colour
    


    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames


# Run everything on repeat after setting up
while True:
    main()