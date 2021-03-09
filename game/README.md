# Schulich Ignite Flare - Game
This game is created over the course of 8 weeks with the help of students learning OOP. It is a collaborative effort between the Ignite team and students and serves as a template for anyone interested in picking up OOP through Pygame.

## Usage
Anyone is encouraged to copy or fork this project for personal use. Commercial usage is prohibited, except when given written consent by Schulich Ignite. While not strictly necessary, we would appreciate if you left the comments in `main.py` crediting the Schulich Ignite team.

## Contributing
You are welcome to create a pull request and add any changes you are interested in. Schulich Ignite reserves the right to make any changes to any contributions without consent from the original author. Schulich Ignite will not claim sole ownership for any contributions.

## Session 1
N/A

## Session 2 - Platforms
Basic platforms have been added in. A fundamental for any platformer game.

## Session 3 - Starting Your Player
Created a player that can move around with the arrow keys and teleport to wherever you click.
For now, the player can walk straight through walls, we'll address that later.

## Session 4 - Updating the Player
Replaced the player created in Session 3 with a player that inherits from the Pygame [sprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) class.

## Session 5 - Jumping Player & Colliding with Platforms
### PRE-BUILT - Platforms have been changed into sprites
The [platform.py](platform.py) file was updated before this session started. The new `Platform` class in [platform.py](platform.py) is now a sprite with an image (be sure to also download and add the [platform_tile.png](assets/platform_tile.png) image to your [assets](assets) folder). This `Platform` sprite repeats the `platform_tile.png` image for any given width and height (best results when your `width` attribute is a multiple of your `height`). Note that the `color` attribute is no longer supported because an image is now being used.

Make sure to download the new file. You will need to also adjust the `platforms` variable in your [main.py](main.py) file to use [sprite groups](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) instead of simple lists. We recommend doing this manually, since it's only a few lines that have been changed. See [changes to SETUP section here](https://github.com/Schulich-Ignite/flare/pull/15/files#diff-b1e8d3adfde20e6d1ec6a75976923fefcf1105bd0ac301404adba2bf76b59557R28-R38) and [changes to DRAW section here](https://github.com/Schulich-Ignite/flare/pull/15/files#diff-b1e8d3adfde20e6d1ec6a75976923fefcf1105bd0ac301404adba2bf76b59557R86). Alternatively, you can just download [main.py](main.py) again and replace your current [main.py](main.py) file, but **please double-check you will not be losing any personal work first**!

### In-class
**Click on [session5_README.md](session5_README.md) for a full explanation of this week.** Gave the player gravity and the ability to jump. The player cannot jump in mid-air and can land on platforms.