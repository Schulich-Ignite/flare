class Eevee:
    def __init__(self,name,type): 
        self.name = name
        self.type = type
    
    def growl(self):
        print(self.name + " used Growl!")
    def tackle(self):
        print(self.name + " used Tackle!")
