# Session 5 Solution
Since we ran out of time during the lectures, this week's solution for the game is written in this document instead. The solution provided goes through step-by-step and doesn't just directly give the answer (if you want the answer, just skip straight to [player.py](player.py) and [main.py](main.py)). Instead we will iterate through a few steps that will let us "discover" a solution. 

Keep in mind that there is no single correct answer (heck, I even change my mind on how to solve these problems half-way through). There are pros and cons to all approaches, some of them which aren't obvious. You could spend an entire university class just learning about how to "best" solve some of these and still not have the best solution.

## Adding in Platform Sprites
We provided an updated version of [platform.py](platform.py) that includes a platform sprite class for you already. This was both to save time and to make an image that can stretch infinitely wide without looking weird. See more details [on the main README.md](https://github.com/Schulich-Ignite/flare/tree/main/game#pre-built---platforms-have-been-changed-into-sprites).

This blurb is to cover some of the changes needed in [main.py](main.py) required to get this working. We first need import our `Platform` class to replace our `platforms` list with a sprite group.
```py
from platform import Platform
```
```diff
- platforms = []

- def add_platform(x, y, width, height, color):
-   p = Platform(x, y, width, height, color)
-   platforms.append(p)
+ platforms = pygame.sprite.Group()

+ def add_platform(x, y, width, height):
+   p = Platform(x, y, width, height)
+   platforms.add(p)
```
Then we need to edit our `add_platform` function to not include a `color` parameter, as well as using `platforms.add(p)` instead of `platforms.append(p)` now that we're using a sprite group.
```diff
- def add_platform(x, y, width, height, color):
-   p = Platform(x, y, width, height, color)
-   platforms.append(p)
+ def add_platform(x, y, width, height):
+   p = Platform(x, y, width, height)
+   platforms.add(p)
```
```diff
- add_platform(300, 600, 350, 50, (100, 255, 100))
- add_platform(100, 500, 200, 50, (50, 100, 255))
- add_platform(650, 450, 200, 50, (50, 100, 255))
+ add_platform(300, 600, 350, 50)
+ add_platform(100, 500, 200, 50)
+ add_platform(650, 450, 200, 50)
+ add_platform(700, 650, 200, 25)
```

Next up is the `update` method...but our platforms have nothing to continuously update, so we can completely skip this step!

Finally we need to replace the manual way of drawing platforms with the sprite group's `platforms.draw(screen)` method.
```diff
- for platform in platforms:
-   pygame.draw.rect(screen, platform.color, platform.rect)
+ platforms.draw(screen)
```

## Making the Player Jump
We covered a lot of this during the session today, so we just need to add the `y_speed` and `gravity` to our player.