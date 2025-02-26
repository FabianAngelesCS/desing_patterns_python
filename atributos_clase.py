
class Auto: #Definiciòn del nombre de la clase.
    className = "Auto" # Este es un atributo de la clase

    # Constructor de la clase para inicializar los atributos con tipo de parametro definido
    def __init__(self, marca: str,  modelo:str):
        self.marca = marca      #tributo que almacena el marca del auto
        self.modelo = modelo    #tributo que almacena el modelo del auto

    def saludo(self): # Mètodo saludo, perteneciente  a la clase.
        print(f"Hello, este es un {self.className}, {self.marca} modelo {self.modelo}") #Mensaje personalizado

Toyota = Auto("Toyota", "Corolla") # Creaciòn de una instancia(Objeto) de la clase 'Auto'

Toyota.saludo() # Llamada al mètodo saludo

# Llamado al atributo de la clase
print(Toyota.className) # Acceso desde una instancia(obejto)
print(Auto.className)   # Acceso desde la clase