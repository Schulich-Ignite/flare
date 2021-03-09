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

Finally we need to replace the manual way of drawing platforms with the `platform` sprite group's `draw(screen)` method.
```diff
- for platform in platforms:
-   pygame.draw.rect(screen, platform.color, platform.rect)
+ platforms.draw(screen)
```

## Making the Player Fall
We covered a lot of this during the session today, so we just need to add the `y_speed` and `gravity` to our player. We'll also toss in an `x_speed` for consistency, even if we're not planning to use it. Let's add those in at the bottom of our player's constructor.
```diff
        self.move_speed = 5
+       self.x_speed = 0
+       self.y_speed = 0
+       self.gravity = 0.6
```

As for the actual falling itself, we will start by putting this inside the player's `update()` method.
```diff
    def update(self):
+       self.rect.y += self.y_speed
+       self.y_speed += self.gravity
```

Last week, our player's `update()` method is getting called inside our `UPDATE` section, so we don't need to update anything in `main.py` to get our player falling.

### Detour - Adding a Method for Falling
The code runs properly at this point, but let's take a quick detour to clean up our code we just typed. This type of "clean up" that changes none of the functionality is called **refactoring** in the programming world. It's like picking up the laundry off the floor and putting it away. Not that it makes your life any more fun right now, but it keeps your room organized (and you wouldn't show your friend a room with dirty socks all over the floor, would you?).

Inside the player's `update()` method, _what_ we want is for the player to fall. _How_ we do this is by changing the player's `y` coordinate and speed. This "what/how" pattern sounds like a good candidate for a method inside `Player` called `fall()`. Let's shuffle the code we wrote in `update()` into `fall()`
```diff
    def update(self):
-       self.rect.y += self.y_speed
-       self.y_speed += self.gravity
+       self.fall()
+
+   def fall(self):
+       self.rect.y += self.y_speed
+       self.y_speed += self.gravity
```

But wait! There's more! Let's repeat the "what/how" on the contents of `fall()` itself. _What_ we want is for the `rect.y` to move down. _How_ we do it...doesn't need to be written from scratch. We can instead use our `move(x_change, y_change)` method we created from before. 
```diff
    def fall(self):
-       self.rect.y += self.y_speed
+       self.move(0, self.y_speed)
        self.y_speed += self.gravity
```

It might look more complicated today, but the beauty is that with OOP, it's flexible. We know that falling involves moving, but if we ever choose to change _how_ we move without caring about _what_ is moving, then we can edit `move(x_change, y_change)` without needing to ever touch `fall()`.

## Making the Player Jump, Part 1
We'll also want to make a way for our player to jump. _What_ we want is the player to jump, _how_ we do it is by instantly changing the `y_speed` to `-15` when the jump starts. Another "what/how" structure, another method inside `Player` that we'll call `jump()`. We can put this code anywhere inside the class...the bottom is a convenient enough spot for now.
```py
    def jump(self):
        self.y_speed = -15
```

And let's change our keyboard events to call this `jump()` method. While we're here, we'll get rid of the movement associated with the down arrow key, that doesn't make sense for our platformer...
```diff
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
-       player.move(0, -player.move_speed)
+       player.jump()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.move(-player.move_speed, 0)
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.move(player.move_speed, 0)
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
-       player.move(0, player.move_speed)
+       pass  # Now that we have platforms, there's no reason to make the player move down.
```

## Colliding With the Platform, Part 1
If you press the play button at this point, you'll notice your player plummet through the floor and sink all the way down to the center of the Earth (ouch, that's gotta be hot). It's time to fix that by adding collisions with our `Platform` sprite. We're going to check which platforms the player collided with by making the variable `hit_platfroms`. Then we're going to set the player's `y_speed` to zero to get our player to stop phasing through solid matter.
I choose to put this code inside the `UPDATE` section of `main.py` because both the player and the platforms are interacting here, neither one "owns" this collision. Not a hard rule, just an opinion. I also chose to put this code after the existing `players.update()` line because the image is less jittery (fall first, then collide/set speed to zero).
```py
    """
    UPDATE section - manipulate everything on the screen
    """
    
    players.update()

    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    if len(hit_platforms) > 0:
        player.y_speed = 0
```

## Side Note - What/How Pattern Isn't a Rule
As an aside, I invented this "what/how" rule by loosely adapting Simon Sinek's TED Talk [How Great Leaders Inspire Action](https://www.youtube.com/watch?v=qp0HIF3SfI4), which is all about communication and nothing about coding. He does a "why/how/what" pattern, and the "why" is _very_ useful when you're starting bigger projects, and his "how" is way less technical. 

Rambling aside, feel free to run with this idea, or if you find something better, feel free to break this "rule".
