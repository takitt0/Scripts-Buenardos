class Animal:
    def __init__(self, name, action):
        self.name = name
        self.action = action
        self.status = "Alive"

    def change_status(self, new_status):
        self.status = new_status
        return self
    
    def make_action(self):
        print(f"{self.name} {self.action}")
        return self
    
perro = Animal("perro", "hace Woof!")
gato = Animal("gato", "hace Miau!")
print("Hallo, Ciao!")

perro.make_action()
gato.make_action()