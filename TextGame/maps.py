
class Map:
    def __init__(self,name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.tiles = {}
    
    def create_map(self):
        for i in self.height:
            for j in self.width:
                self.tiles[(i,j)] = []

class Tiles:
    Objects = ["Rock", "Swamp"]

    def __init__(self, tile):
        self.tile = tile
    
    def check(self):
        for obj in self.Objects:
            if obj in self.tile:
                return False
    
        

    

       
        