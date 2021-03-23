import pygame

class Level:
    def __init__(self, platform_list, enemy_list, player_spawn=(400, 500)):
        """
        Create a new level

        Args:
            platform_list: A list of platform objects that will be stored as the platforms sprite group
            enemy_list: A list of enemy objects that will be stored as the enemies sprite group
            player_spawn: A tuple (x, y) to store the coordinates that the player should spawn at at the start of the level. Defaults to (400, 500)
        """
        self.platforms = pygame.sprite.Group(platform_list)
        self.enemies = pygame.sprite.Group(enemy_list)
        self.player_spawn = player_spawn

    def start(self, player):
        """
        Start the level. Move the player to the spawn location and clear the player's bullets
        
        Args:
            player: The player to move and clear the bullets from
        """
        player.rect.x = self.player_spawn[0]
        player.rect.y = self.player_spawn[1]
    
        # Clear the list of existing bullets
        player.bullets.empty()
        