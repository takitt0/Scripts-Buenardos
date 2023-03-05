class Animal:
    def __init__(self, name, action):
        self.name = name
        self.action = action
<<<<<<< HEAD
        self.status = 'Alive'
        
    def accion(self):
        print(f"{self.name} is doing this: {self.action}")
=======
        self.status = "Alive"

    def make_action(self):
        print(f"{self.name} {self.action}")
>>>>>>> classtest

perro = Animal("perro", "hace Woof!")
print("Hallo world desde el main!")