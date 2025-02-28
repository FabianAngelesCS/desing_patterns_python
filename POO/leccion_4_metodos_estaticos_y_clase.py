

class Auto: #Definiciòn del nombre de la clase.
    className = "Auto" # Atributo de la clase

    # Constructor de la clase para inicializar los atributos con tipo de parametro definido
    def __init__(self, marca: str,  modelo:str):
        self.marca = marca      #tributo que almacena el marca del auto
        self.modelo = modelo    #tributo que almacena el modelo del auto

    def saludo(self): # Mètodo de instancia (requiere 'self').
        print(f"Hello, este es un {self.className}, {self.marca} modelo {self.modelo}") #Mensaje personalizado

    @staticmethod   # Mètodo estàtico: no usa 'self' ni 'cls' y es independiente de la isntancia,
    def Hello_world():
        print("Hello world, este mensaje proviene de un método estático.")

    @classmethod   # Mètodo de la clase: recibe 'cls'y puede acceder a los atributos de la clase.
    def hello_wordl2(cls):
        print(f"Hello world, este mensaje proviene de un método de clase. Clase: {cls.className}")
#Creaciòn de una isntancia de la clase 'Auto'
Toyota = Auto("Toyota", "Corolla") # Creaciòn de una instancia(Objeto) de la clase 'Auto'

Toyota.saludo() # Llamada al mètodo de la instancia.
Toyota.Hello_world() # llamar al metodo estatico deesde la isntancia.
Auto.Hello_world()   # Llamar al metodo estaticpo desde la clase.

Toyota.hello_wordl2() # Llamar al mètodo de la clase desde la isntancio
Auto.hello_wordl2()   # Llamar al mètodo de la clase desde la clase