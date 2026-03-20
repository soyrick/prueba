from seres_vivos.ser_vivo import SerVivo    

class Mamifero(SerVivo):
    def __init__(self, name, specie, age, habitat, gestation_period):
        super().__init__(name, specie, age, habitat)
        self.gestation_period = gestation_period
        self.warm_blooded = True
    #parir en periodo de gestacion   
    def give_birth(self):
        if self.alive:
            print(f"{self.name} is giving birth after a gestation period of {self.gestation_period} months.")
        else:
            print(f"{self.name} is not alive and cannot give birth.")
            
    #eat
    def eat(self, food):
        if self.alive:
            print(f"{self.name} is eating {food}.")
        else:
            print(f"{self.name} is not alive and cannot eat.")
    #sleep
    def sleep(self, hours):
        if self.alive:
            print(f"{self.name} is sleeping for {hours} hours.")
        else:
            print(f"{self.name} is not alive and cannot sleep.")
    #mostrar informacion del mamifero
    def show_info(self):
        super().show_info()
        print(f"Gestation Period: {self.gestation_period} months")
        print(f"Warm Blooded: {'Yes' if self.warm_blooded else 'No'}")
        