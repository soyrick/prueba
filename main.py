from seres_vivos.ser_vivo import SerVivo
from mamiferos.mamifero import Mamifero    
from personas.persona import Persona   

def main_poo():
    # Crear un ser vivo 
    ruperto = SerVivo("Ruperto", "Perro", 5, "Casa")
    ruperto.show_info()
    print("\n")
    # Crear un mamifero
    lola = Mamifero("Lola", "Gato", 3, "Casa", 2)
    lola.show_info()
    print("\n")

    # Crear una persona
    juan = Persona("Juan", 25, "Ciudad", 9, "25", "Ingeniero")
    juan.show_info()
    
if __name__ == "__main__":
    main_poo()