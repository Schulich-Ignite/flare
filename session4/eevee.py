# Session 4 Exercise 1 - Jolteon
# This is the base class Eevee we built in lectures.
# Use this to create a class Jolteon that inherits from Eevee
class Eevee:
    def __init__(self, name, type): 
        self.name = name
        self.type = type
    
    def growl(self):
        print(self.name + " used Growl!")

    def tackle(self):
        print(self.name + " used Tackle!")
