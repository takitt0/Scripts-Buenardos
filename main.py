import random

class Objeto:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Equipado {self.name}!"

class Animal:
    def __init__(self, name, action):
        self.name = name
        self.action = action
        self.status = random.choice(["Alive", "Dead"])
        self.mochila = []

    def equipar(self, objeto):
        if isinstance(objeto, Objeto):
            self.mochila.append(objeto)
        
        return self

    def change_name(self, new_name):
        self.name = new_name
        return self

    def change_status(self, new_status):
        self.status = new_status
        return self
    
    def make_action(self):
        print(f"{self.name} {self.action}")
        return self
    
    def __repr__(self):
        return f"Roberto saluda a {self.name} y esta {self.status}!"

if __name__ == "__main__":    
    perro = Animal("perro", "hace Woof!")
    gato = Animal("gato", "hace Miau!")
    pala = Objeto("Pala")
    print("Hallo, Ciao!")

    print(perro.status)
    gato.make_action()
    gato.equipar(pala)
