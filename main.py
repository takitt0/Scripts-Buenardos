class Animal:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def run(self):
        print(f"{self.name} {self.action}")

perro = Animal("perro", "hace Woof!")
print("Hallo world desde el main!")