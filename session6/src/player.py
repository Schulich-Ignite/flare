import pygame
import os


GRAVITY = 0.25
JUMP_VELOCITY = -1 * 12


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image, set class rectangle to that of the image
        image_location = os.path.join("assets", "player.png")  # Find the path of the player image
        self.image = pygame.image.load(image_location).convert_alpha()  # load the image
        self.rect = self.image.get_rect()  # get the rect of the image
        
        # Set the initial position of the player
        self.rect.x = 400  # have the player start at 400 on x axis
        self.rect.y = 0 # this is initialized for us (self.image.get_rect()), but you can change it if you want

        # Physics       
        self.jump_cooldown = 0  # the player can jump right away!
        # speed (change in position per tick)
        self.x_speed = 5  # speed in the x direction
        self.y_speed = 0  # speed in the y direction

    # how do we want to implement the other actions?

    # Parameters:
    #   - keyspressed - result of pygame.key.get_pressed(), passed in from main
    def update(self, keys_pressed):

        # If you want, feel free to seperate the sections out into different methods.
        # I prefer to keep it all together so you don't have to worry about how it fits together.

        # SETUP  -------------------------------------
        # End of SETUP

        # EVENTS -------------------------------------

        # Recall: keys_pressed is passed to us from the main loop
        # You can check for keys pressed as usual!

        # Reset direction so that the player stops moving when keys not pressed
        direction = [0, 0]
        if keys_pressed[pygame.K_UP]:
            direction[1] = -1  # y direction goes up
        if keys_pressed[pygame.K_DOWN]:
            direction[1] = 1  # y direction goes down
        if keys_pressed[pygame.K_LEFT]:
            direction[0] = -1  # x direction goes left
        if keys_pressed[pygame.K_RIGHT]:
            direction[0] = 1  # x direction goes right

        # Handle jump events
        if keys_pressed[pygame.K_SPACE]:
            # This will run if SPACE is pressed
            if self.jump_cooldown == 0:  # This will run if jump_cooldown is 0
                self.jump_cooldown = 30  # Reset the cooldown to 30 frames
                self.y_speed += JUMP_VELOCITY  # Add velocity for the jump (must be greater than gravity to work properly)
        
        # End of EVENTS
        # UPDATES ------------------------------------

        self.rect.x += direction[0] * self.x_speed
        # self.rect.y += direction[1] * self.speed
        # Remove gravity, jump code & uncomment the above line to remove platformer physics

        self.y_speed += GRAVITY  # Add gravity to y_speed
        self.rect.y += self.y_speed  # Add speed to position

        # If jump_cooldown is >= 1, subtract by 1 to lower the cooldown
        # this happens every frame, so jump_cooldown is the number of frames 
        # the player must wait to jump again after jumping.
        # When jump_cooldown is 0, we can jump again!
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

        # End of updates

    # Teleport to mouse position
    # Parameters:  
    #   - mousepos - the position of the mouse (passed in from main)
    def teleport(self, mousepos):
        x = mousepos[0]
        y = mousepos[1]
        self.rect.x = x
        self.rect.y = y
