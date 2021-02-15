# Session 2 Exercise 1
# Pre-made code Tree
# 
# from Tree import tree  # <--- Add this line at the top of your main file
# tree = Tree()          # <--- Add this line in the main file to create a new Tree object

class Tree:
    def __init__(self):
        self.trunk_x = 0
        self.trunk_y = 0
        self.leaves_x = 0
        self.leaves_y = 0
        self.leaves_size = 0
        self.leaves_color = (0, 0, 0)  # Note American spelling of "colour". You can edit this to "self.leaves_colour" if you prefer Canadian style


        # -------------- BONUS ------------------
        # branches is a list of leaves, written as tuples. Can you add some branches and draw them all?
        # You can ignore the colour
        # Tuple structure: (x, y, size)
        self.branches = [(0, 0, 0)]
        self.has_branches = False  # You can ignore this, used to decide which tree is drawn