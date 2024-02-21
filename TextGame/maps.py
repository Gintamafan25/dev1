
class Map:
    def __init__(self,name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.tiles = {}
    
    def create_map(self):
        for i in range(self.height):
            for j in range(self.width):
                self.tiles[(i,j)] = [Tile(i,j)]

class Tile:
    

    def __init__(self, coords):
        self.tile = coords
        self.objects = []
    
    def add_object(self, obj):
        self.objects.append(obj)
    
    def check(self):
        return len(self.objects) == 0

    
        

    

       
        