# A la izquierda tienes el archivo __init__.py, eso es para que el directorio 'seres_vivos' sea tratado como un paquete en Python. El archivo __init__.py puede estar vacío o contener código de inicialización para el paquete. y se usa para poder usar este paquete dentro de otros archivos 

class SerVivo:
    def __init__(self, name, specie, age, habitat):
        self.name = name
        self.specie = specie
        self.age = age  
        self.habitat = habitat
        self.alive = True

    def eat(self,food):
        if self.alive:
            print(f"{self.name} is eating {food}.")
        else:
            print(f"{self.name} is not alive and cannot eat.")
            
    def sleep(self, hours):
        if self.alive:
            print(f"{self.name} is sleeping for {hours} hours.")
        else:
            print(f"{self.name} is not alive and cannot sleep.")
            
#mostrar informacion del ser vivo 
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Specie: {self.specie}")
        print(f"Age: {self.age} years")
        print(f"Habitat: {self.habitat}")
        print(f"Alive: {'Yes' if self.alive else 'No'}")