
class Animal: #Definiciòn del nombre de la clase.

    # Constructor de la clase para inicializar los atributos con tipo de parametro definido
    def __init__(self, name: str,  habitat:str):
        self.name = name
        self.habitat = habitat

    def saludo(self): # Mètodo saludo, perteneciente  a la clase.
        print(f"Hello, {self.name} tù vives en la {self.habitat}") #Mensaje personalizado

leon = Animal("Leon", "sabana") # Creaciòn de una instancia(Objeto) de la clase 'Animal'

leon.saludo() # Llamada al mètodo saludo