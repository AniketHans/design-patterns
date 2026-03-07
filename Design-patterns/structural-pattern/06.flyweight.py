'''
    The Flyweight Design Pattern is a structural design pattern used to reduce memory usage by sharing common objects instead of creating many identical ones.
    It is useful when an application needs to create a very large number of similar objects.
    
    Imagine a text editor.
    Each character may store:
        character
        font
        size
        color
        position
    If you have 1 million characters, storing everything per character wastes memory.
    
    Instead:
    Shared (Flyweight):
        font
        size
        color
    Unique:
        character
        position
    
    Basically, we just put the common properties in a separate object and reuse the object with the uncommon properties
'''

# Flyweight

# Tree type in gaming env
class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def display(self, x, y):
        print(f"Tree {self.name} ({self.color}) at ({x},{y})")
    
# Tree factory
# It ensures object reuse

class TreeFactory:
    _trees ={}
    
    @classmethod
    def get_tree(self, name, color):
        key = (name,color)
        
        if self._trees.get(key) == None:
            t = TreeType(name, color)
            self._trees[key]=t
        return self._trees[key]

class Tree:
    def __init__(self, x:int, y:int, tree_type:TreeType):
        self.x=x
        self.y=y
        self.tree_type=tree_type
    
    def draw(self):
        self.tree_type.display(self.x, self.y)

trees = []
for x in range(100):
    tree_type = TreeFactory.get_tree("Oak", "Green")
    trees.append(Tree(x,x+1,tree_type))

for tree in trees[:10]:
    tree.draw()
    