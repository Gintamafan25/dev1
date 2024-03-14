
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
    
    def show_map(self):
        for i in range(self.height):
            for j in range(self.width):
                if Tile((i,j)).objects == "Blocked":
                    print("X",end="")
                else:
                    print(" ", end="")
            print("")

class Tile:
    

    def __init__(self, coords):
        self.tile = coords
        self.objects = []
    
    def add_object(self, obj):
        if obj not in self.objects:
            self.objects.append(obj)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
    
    def check(self):
        if "Blocked" in self.objects:
            return True
        else:
            return False

    
        

    

       
        