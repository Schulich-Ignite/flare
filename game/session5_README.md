# Session 5 Solution
Since we ran out of time during the lectures, this week's solution for the game is written in this document instead. The solution provided goes through step-by-step and doesn't just directly give the answer (if you want the answer, just skip straight to [player.py](player.py) and [main.py](main.py)). Instead we will iterate through a few steps that will let us "discover" a solution. As a warning, that means deleting and re-writing some lines of code, including lines we just wrote seconds ago!

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
+ add_platform(700, 650, 200, 25)  # Fourth thin platform added just for fun
```

Next up is the `update` method...but our platforms have nothing to continuously update, so we can completely skip this step!

Finally we need to replace the manual way of drawing platforms with the `platform` sprite group's `draw(screen)` method.
```diff
- for platform in platforms:
-   pygame.draw.rect(screen, platform.color, platform.rect)
+ platforms.draw(screen)
```

## Making the Player Fall
We covered a lot of this during the session today, so we just need to add the `y_speed` and `gravity` to our player. We'll also toss in an `x_speed` for consistency, even if we're not planning to use it. Let's add those in at the bottom of our `Player` constructor.
```diff
    def __init__(self, x, y):
        
        ...

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

Inside the player's `update()` method, _what_ we want is for the player to fall. _How_ we do this is by changing the player's `y` speed. This "what/how" pattern sounds like a good candidate for a method inside `Player` called `fall()`. Let's shuffle the code we wrote in `update()` into `fall()`
```diff
    def update(self):
        self.rect.y += self.y_speed
-       self.y_speed += self.gravity
+       self.fall()
+
+   def fall(self):
+       self.y_speed += self.gravity
```

As for the other line, `self.rect.y += self.y_speed`, that looks identical to one of our lines inside the `move(x_change, y_change)` method we already have. Generally we want to avoid repeating our code, so let's instead re-use the `move()` method with this `y_speed` as the input. We'll also toss in `x_speed` as the x parameter.
```diff
    def update(self):
-       self.rect.y += self.y_speed
+       self.move(self.x_speed, self.y_speed)
        self.fall()

    def fall(self):
        self.y_speed += self.gravity
```

_Note: This decision is purely subjective, we could have added this `move()` line inside the `fall()` method instead. There won't ever be a definite_ right _answer, just the answer that makes the most sense to you at the time._

Reading it over, let's make sure _what_ we want makes sense inside the `update()` method. _What_ it does is move the player based on their current speed, and then we factor in the falling. It's always a good sanity check whenever you're cleaning up your code to make sure the end result matches what you want, regardless of how you choose to do it. It might look more complicated today, but the beauty is that with OOP, it's flexible. We know that falling involves moving, but if we ever choose to change _how_ we move without caring about _what_ is moving, then we can edit `move(x_change, y_change)` without needing to ever touch `update()` or `fall()`.

## Making the Player Jump
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

## Colliding With the Platform
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

And once we wrap this up, **we're done the main challenge**! We can stop here. Orrr...join me on the solution for the first bonus, which explains a few subtle differences between what we just worked through and the answers found in [main.py](main.py) and [player.py](player.py).

## Bonus 1 - Preventing Jumping in Mid-Air
Much as I love ~~Flappy~~ Ignitey Bird, we should figure out a way to prevent the player from hopping in mid-air. I'll break out the "what/how" pattern again, this time using it to figure out _what_ we want and then using that to solve _how_. The key for this _what_ part is to be specific, which will help find insights on _how_ to do it.

_What_ we want is for the player to not jump in mid-air. That means they should only be able to jump from the ground. Aaaaand that's about as detailed as I can get for the _what_. As I typed this out, I realized I was getting so specific, I was jumping into the _how_. Might as well embrace it. _How_ do we know if we can jump? We need a definition for "can jump" and "can't jump". 

It's reasonable to say that "can jump" means the player is on the ground, and "can't jump" means the player is in mid-air. Back in our code, we should get an `if` statement that's controlled by a member variable `can_jump`. Let's define this member variable inside the `Player` constructor, and initialize it to be `True`.
```diff
    def __init__(self, x, y):
        
        ...

        self.move_speed = 5
        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 0.6

+       self.can_jump = True
```

Now the `if` statement to control whether the jumping actually happens. I'm going to choose to put this inside the player's `jump()` method (another reasonable choice is in the key events, where you call `player.jump()`. Again, personal preference only).
```diff
    def jump(self):
-       self.y_speed = -15
+       if self.can_jump:
+           self.y_speed = -15
```

Let's also control when the member variable `self.can_jump` is `True` and `False`. When can we jump? When we're on the ground. Let's add onto our collision with platform logic in the `UPDATE` section and change the `can_jump` variable there. Furthermore, let's say when there's no collisions between the player and the platforms, then they can't jump.
```diff
    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    if len(hit_platforms) > 0:
        player.y_speed = 0
+       player.can_jump = True
+   else:
+       player.can_jump = False
```

## Adjusting Collision Logic
For the keen-eyed among you, you may discover that sometimes the player gets wedged into the platform instead of sitting on top. This is because the player doesn't continuously move like in the real world, rather they move in a discrete number of pixels. Let the player drop from high enough and they won't collide with the top of the platform but the middle of the platform. There are some ways to change the player's motion to be continuous, but that's too advanced for these sessions, so the next best thing is to correct the player's y coordinate when they hit the platform.

What we need to do during our collisions is to set the player's position to the top of the platform. How we do this is a bit more complex than just setting the y coordinate, because:
1. We need to know which platform we're colliding with. So far, we only know when our player collides with a platform.
2. All coordinates for sprites refer to the top-left corner, but we want to align the player's feet to be just above the platform.

Solving issue #1 is actually simple - the `hit_platforms` gives us a list of all the platforms the player has currently hit. And assuming the platforms are spread apart, that's usually just a list of one! We can replace our `if len(hit_platforms) > 0` with a `for` loop instead, but we'll need to remember the `else` statement changes into `if len(hit_platforms) == 0` once we remove the original `if` statement. Or, for those of you familiar with Python's "truthy" and "falsey" rules, you can instead replace the `else` statement with `if not hit_platforms` to be more pythonic with it.
```diff
    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
-   if len(hit_platforms) > 0:
+   for platform in hit_platforms:
        player.y_speed = 0
        player.can_jump = True
-   else:
+
+   if len(hit_platforms) == 0:
        player.can_jump = False
```

Solving issue #2 is just a matter of simple math, now that we know where the hit platform is. We can get the player's height with `player.rect.height`. Subtract that height from `platform.rect.y` et voila! Instant corrected player y coordinate!
```diff
    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    for platform in hit_platforms:
+       player.rect.y = platform.rect.y - player.rect.height
        player.y_speed = 0
        player.can_jump = True

    if len(hit_platforms) == 0:
        player.can_jump = False
```

### Detour - Cleaning Up Collision Logic
Once again, the code inside the collision isn't obvious. _What_ it's supposed to be doing is stopping the player from falling, but when we read the code, we're just seeing _how_ it's done, leaving the next person to decipher all the math we've added. Let's wrap this into a method inside `Player` class called `on_platform_collide()` and pass in the platform as a parameter.
```py
    # Class Player in player.py
    def on_platform_collide(self, platform):
        # Need to set self.rect.y explicitly to avoid having the player clip through the floor
        self.rect.y = platform.rect.y - self.rect.height
        
        self.y_speed = 0
        self.can_jump = True
```

And of course, we call this new method in our `for` loop.
```diff
    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    for platform in hit_platforms:
-       player.rect.y = platform.rect.y - player.rect.height
-       player.y_speed = 0
-       player.can_jump = True
+       player.on_platform_collide(platform)

    if len(hit_platforms) == 0:
        player.can_jump = False
```

As noted in the code for [player.py](player.py), there's a new issue that's optional for you to solve: 
> `Note a new bug surfaces - players jumping from the underside will teleport to the top. This is left for students to solve if interested`

Any collision with the platform assumes it will always be from above. Which isn't always the case when you have floating platforms. I'm not solving it here because that's too specific for this example program. If you choose to solve it yourself, you can either make the player pass through the platform as they're jumping up, or treat all edges of the platform as solid, and push the player out to the nearest edge. Feel free to ask your mentors for more help if you get stuck solving this!

### Detour - Cleaning Up Jumping by Escaping Early
Many people (including professional software engineers) would say the code for `jump()` is good and proper at this point. But I'm lazy, so I prefer a slightly different style. I prefer code where I don't need to press the indent button so much. And as an even stronger motivation, I prefer code where I don't need to memorize as much to understand what's going on. I want code that's easy to read and easy to write. So I'm going to refactor again by doing a double-negative trick.
```diff
    def jump(self):
-       if self.can_jump:
-           self.y_speed = -15
-           self.can_jump = False
+       if not self.can_jump:
+           return
+       self.y_speed = -15
```

Now with this, we don't have to worry about keeping track of whether or not we "can jump" while we're in the middle of jumping. If you're not convinced, just read the upcoming seriuos detour.

#### Serious Detour - Off in the Weeds Explaining Why
This new code looks more convoluted than before, but that's because this is a tiny example. If I wanted a better example, I would show one where jumping isn't as simple as one line like  `self.y_speed = -15` but one that involves dozens more lines. Prepare to read an example made far more complicated than necessary...
```py
    # Some hypothetical, complicated version of jumping. DON'T COPY THIS
    def complicated_jump(self):
        if not self.can_jump:
            return  # <-- Escape early. If the player can't jump, then don't bother reading the rest
        self.y_speed = -15

        # Hypothetical stuff to make jumping cool
        self.set_animation("jump_animation.png")
        self.play_sound("jump")
        platform_material = self.get_material(self.platform)
        for i in range(10):
            dirt_x = random.randint(10) - 5 + self.rect.x
            if coordinate_on_platform(dirt_x, self.rect.y):
                draw_dirt_particle(dirt_x, self.rect.y + self.rect.height)  # <-- Observe how "indented" the code is at this point!
```

My crazy example adds way more features to our jump (which isn't uncommon when you start doing bigger projects). Way down deep in the weeds, you might be reading some complicated code about drawing dirt particles if they're on the platform. At this point, you don't want to be burdened with also remembering "all of this can only happen if `self.can_jump` is also `True`". The more things you need to remember, the more things you'll probably forget.

Hence, my rule of thumb - if there's a chance that it doesn't happen (e.g. `can_jump` is `False`) then keep it out of your code where it does happen. Escape from your functions early.

## Closing Thoughts - The "What/How" Pattern Isn't a Rule
As an aside, I invented this "what/how" rule by loosely adapting Simon Sinek's TED Talk [How Great Leaders Inspire Action](https://www.youtube.com/watch?v=qp0HIF3SfI4), which is all about communication and nothing about coding. He does a "why/how/what" pattern, and the "why" is _very_ useful when you're starting bigger projects, and his "how" is way less technical. 

Rambling aside, feel free to run with this idea, modify this idea, or if you find something better, ignore it. And if you do find a better pattern, I definitely would love to learn it from you! 😄
