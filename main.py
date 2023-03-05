class Animal:
    def __init__(self, name, action):
        self.name = name
        self.action = action
        self.status = 'Alive'
        
    def accion(self):
        print(f"{self.name} is doing this: {self.action}")

perro = Animal("perro", "hace Woof!")
print("Hallo world desde el main!")