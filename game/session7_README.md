# Session 7 Solution

> _During Session 7, I had made a few mistakes on the function `next_level()`. I was unable to create a valid fix during the session, which ultimately led to a non-functional function and some very confused students. These mistakes are rare, but we strive to deliver high quality to you in every session. I ask you to not let this reflect on the quality of your mentors or the organization as a whole; our team has very dedicated volunteers working on this and we take several steps to ensure issues like these do not arise. Out of bad judgement, I skipped some of our final checks, which allowed for these errors to surface in the sessions. I personally apologize for this mistake and take full responsibility. I also promise to work hard to prevent issues like this from ever happening again._
>
> _Richard Lee_

This write-up is an explanation of why the code written in the function `next_level()` as seen during our Session 7 did not work, and provides one fix. 

This write-up is also an opportunity to elaborate on a few improvements that have been added to the game, but are not critical for you to understand, namely:
* Changes to `Level`:
  * Adding a `player_spawn` parameter to the constructor
  * Adding a `start()` method to `Level`.
* Changes to `Bullet`:
  * Changing bullets to shoot left or right
  * Removing bullets that stray off-screen to save computer resources

## tl;dr - The Fix For `next_level()`
Update the `next_level()` function as follows:
```py
levels = [Level(...), Level(...)]
level = levels[0]

def next_level(levels):
    new_level = levels[levels.index(level) + 1]
    return new_level

# Later we call the function
level = next_level(levels)
```
An explanation for what failed and why this solution works is provided below.

## Why `next_level()` Failed During the Session
To understand why the correct solution for `next_level()` works and why it was designed the way it was, it helps to understand why the attempted solution failed in the first place. Feel free to skip this section if you already understand the issue or are generally uninterested.

### Iteration 1 - Bad Variable Scope in Functions
Let's look at the first iteration, as was presented in the slides (note - the slides may already be updated to the correct version by the time you read this).
```py
# ERROR: THIS CODE FAILS
levels = [Level(...), Level(...)]
level_number = 0
level = levels[level_number]

def next_level():
    level_number += 1
    level = levels[level_number]
```

The issue is variable scope; the variable named `level_number` on the line `level_number += 1` is completely different from the variable with the same name `level_number = 0` a few lines above. The same goes for the `level` variable underneath. Funny enough, there is only one `levels` variable, despite it basically being used the same way as the other two variables.

The difference between the working `levels` variable versus the failing `level_number` and `level` variables is that `levels` is only being _read_ from while the first two are being _written into_. Python treats these as two different scenarios. In my personal opinion, this is not a good thing and can lead to many design traps (like the one I encountered).

When Python sees a variable being used (in this case `levels[...]`), it searches for the definition of the variable. It finds `levels` defined outside of `next_level()`, so it assumes that the `levels` inside `next_level()` is the same thing. In other words, it uses the **global** `levels` definition. This works as we expect.

But problems arise when when try doing the same thing while assigning values to variables. Any time we have an `=` assignment operator (or the `+=` increment operator) inside a function, the variable being assigned to is a brand new variable, hidden from the rest of the code. This is great for modular code; we don't have to care about where names are repeated, we can assume our code inside our `next_level()` function _doesn't_ impact any code outside of the function. But this is terrible if we _do_ want to impact the variables outside the function.

The following lines are the same as above, but split down onto multiple lines so I can fit some comments in.
```py
# ERROR: THIS CODE FAILS
levels = [Level(...), Level(...)]  # Let's call this GLOBAL levels
level_number = 0                   # And call this GLOBAL level_number
level = levels[level_number]       # And call this GLOBAL level

def next_level():
    level_number += 1              # Let's assign a new LOCAL level_number variable

    level =                        # And assign a new LOCAL level variable
        levels[                    # This is only being read from, this is GLOBAL levels
            level_number           # We use the "nearest" definition. We use the LOCAL level variable
        ]
```

Confused? So am I. We have some **global** and **local** variables with the same name but different values. Any time you are getting confused by code is a strong indicator that it's bad code. 

### Iteration 2 - Make EVERYTHING Global
I started this solution during our sesson but abandoned it because it's generally frowned upon. That being said, if you want a quick and dirty solution, then the following solution is perfectly functional. We can use the Python keyword `global` to clearly state our intention to Python: "Please use the **global** variable inside the function". We'll ask that `level_number` and `level` to be treated as **global** variables. To play it safe, we'll also ask `levels` to be treated as a **global** variable, even though it already is.
```py
# WARNING: This code works but is not recommended
levels = [Level(...), Level(...)]  # Let's call this GLOBAL levels
level_number = 0                   # And call this GLOBAL level_number
level = levels[level_number]       # And call this GLOBAL level

def next_level():
    global levels, level_number, level  # Treat all these variables as GLOBAL

    level_number += 1                   # Increment the GLOBAL level_number
    level = levels[level_number]        # Assign the GLOBAL level from the GLOBAL levels
```

Some of you may be thinking, "So why's this bad? It's a concise and clear answer." The answer is that this breaks _modularity_; it breaks the idea that code should be packaged into small independent modules that should not interact with one another. This example is easy to read because it's so short and the definition of the global variables is nearby the `next_level()` function. 

But as all bad design decisions go, it's easy to start, but regrettable later. If you add a ton of code later on, some of it using `global level`, some of it using `global level_number`, and so on, then it might work...but it soon becomes very difficult to remember what code is interacting with your `level` and `level_number` variables. It might be set to a surprising value (maybe `level_number = -999` is buried in your code somewhere), and it becomes impossible to know what the value of the variables are, much less _trust_ that they are what you expect. Which leads to a good rule: **Avoid global variables as much as possible**. 

Python was designed for quick scripting, so it lets us get away with global variables, but other languages, like Java or C#, strictly forbid them altogether. And for good reason, they lead to messes like this.

### Iteration 3 - Pass the Global Variables As Arguments
What if instead of using the `global` keyword, we just tried feeding the global variables into the `next_level()` function as arguments? I tried this method out...and promptly realized that this was a bad idea (and this is where I gave up). The arguments supplied to a function _also_ have special rules on variable scope. The rules are similar to global variables; you can read from a parameter to get its argument, but if you try re-assigning one, you just get a local variable, and the original parameter is left unchanged.
```py
# ERROR: THIS CODE FAILS
levels = [Level(...), Level(...)]
level_number = 0
level = levels[level_number]

def next_level(level_number, level):  # This is PARAM level_number (same as GLOBAL level_number)
                                      # And     PARAM level        (same as GLOBAL level)

    level_number += 1                 # We can't re-assign the PARAM level_number (0), so we instead change the value
                                      # and store it in a LOCAL level_number (1)
    
    level = levels[level_number]      # Same goes for the PARAM level (level 0). We can't change the value
                                      # And just make a LOCAL level (level 1)


# Later we call the function and pass
# the GLOBAL level_number and level in as arguments
next_level(level_number, level)
```
Behind the scenes, the `=` assignment operator is changing _pointer_ references. But that's a very big topic for another day. Long-story short, this doesn't work, and both the **global** `level_number` and `level` is left at its original level.

## Solution to `next_level()` Function
The proper solution should not attempt to change the global variable `level`. We do have a work-around, and this one is completely valid: _return_ the next level and let the global `level` be changed in a separate section of the code. Along the way, we can completely throw out the `level_number` varible because it was only use to find the appropriate level in our list of `levels` anyway. Less variables = less things to lose track of. We'll take advantage of the `levels.index()` function to calculate our level number.
```py
levels = [Level(...), Level(...)]
level = levels[0]

def next_level():
    current_level_number = levels.index(level)
    new_level_number = current_level_number + 1
    new_level = levels[new_level_number]
    return new_level

# Later we call the function and
# directly edit the GLOBAL level. 
# No messy LOCAL level variable to get confused with!
level = next_level()
```

Almost done, let's make some minor improvments. I don't trust reading a global variable, even though this code works fine. So I'll pass in `levels` as an argument. I'l also condense the `current_level_number`, `new_level_number` and `new_level` into a single line of equivalent code.
```py
levels = [Level(...), Level(...)]
level = levels[0]

def next_level(levels):
    new_level = levels[levels.index(level) + 1]
    return new_level

# Later we call the function
level = next_level(levels)
```

This is not the only good answer; there are other methods, like using an iterator, but those require more Python skill that goes beyond the scope of this session.