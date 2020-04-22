class Object:
    def __init__(self, color, name):
        self.name = name
        self.color = color

class Object_3:
    def __init__(self, fight):
        self.fight = fight

class Object_2(Object_3, Object):
    pass
    
print(+-1)
