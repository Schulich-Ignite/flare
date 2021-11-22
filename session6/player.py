import pygame
import os


GRAVITY = 0.25
JUMP_VELOCITY = -1 * 12


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image, set class rectangle to that of the image
        image_location = os.path.join("assets", "player.png")  # Find the path of the player image
        self.image = pygame.image.load(image_location).convert_alpha()  # Load the image
        self.rect = self.image.get_rect()  # Get the rect of the image
        
        # Set the initial position of the player at (400, 600), just above a platform
        self.rect.x = 400
        self.rect.y = 600

        # Speed (change in position per tick)
        self.x_speed = 5  # Movement speed in the x direction (must be greater than 0, or you won't move!)
        self.y_speed = 0  # Movement speed in the y direction 

        # Physics       
        self.jump_cooldown = 0  # The player can jump right away!

    def update(self, keys_pressed, mouse_buttons, mouse_pos):
        """
        Update the player

        Args:
            keyspressed: Result of pygame.key.get_pressed(), passed in from main
        """

        # If you want, feel free to seperate the sections out into different methods.
        # I prefer to keep it all together so you don't have to worry about how it fits together.

        # SETUP  -------------------------------------

        teleport = False  # Must reset to False, or else the player will keep teleporting to the cursor after the first click
        direction = [0, 0]  # Reset direction so that the player stops moving when keys not pressed

        # End of SETUP

        # EVENTS -------------------------------------

        # Recall: keys_pressed is passed to us from the main loop
        # You can check for keys pressed as usual!
        # Reset direction so that the player stops moving when keys not pressed

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
        
        # Set teleport to True if we need to call teleport() in update!
        if mouse_buttons[0]:  # If left mouse pressed
            teleport = True  
        if mouse_buttons[2]:  # If right mouse pressed
            teleport = True

        # End of EVENTS
        # UPDATES ------------------------------------

        # Check if we need to teleport
        if teleport:
            self.teleport(mouse_pos) # if True, teleport to mouse position

        self.rect.x += direction[0] * self.x_speed
        # self.rect.y += direction[1] * self.speed
        # Remove gravity, jump code & uncomment the above line to remove platformer physics

        self.y_speed += GRAVITY  # Add gravity to y_speed
        self.rect.y += self.y_speed  # Add speed to position

        # If jump_cooldown is >= 1, subtract by 1 to lower the cooldown
        # This happens every frame, so jump_cooldown is the number of frames 
        # the player must wait to jump again after jumping.
        # When jump_cooldown is 0, we can jump again!
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

        # End of updates

    def teleport(self, mousepos):
        """
        Teleport to mouse position

        Args:
            mousepos: The position of the mouse as a tuple representing (x, y), passed in from main
        """
        x = mousepos[0]
        y = mousepos[1]
        self.rect.x = x
        self.rect.y = y
