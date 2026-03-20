from mamiferos.mamifero import Mamifero

class Persona(Mamifero):
    def __init__(self, name, age, specie,habitat, gestation_period, occupation):
        super().__init__(name, specie,  age, habitat, gestation_period)
        self.occupation = occupation
        self.think = True
        
    def work(self):
        if self.alive:
            print(f"{self.name} is working as a {self.occupation}.")
        else:
            print(f"{self.name} is not alive and cannot work.")
    def eat(self, food):
        return super().eat(food)
    def sleep(self, hours):
        return super().sleep(hours)
    
    def show_info(self):
        super().show_info()
        print(f"Occupation: {self.occupation}")
        print(f"Think: {'Yes' if self.think else 'No'}")