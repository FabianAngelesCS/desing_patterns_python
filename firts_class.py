

# Esta es la estrutura bàsica de una clase de Python.
class Person: #Definiciòn del nombre de la clase.

    def __init__(self, name): #Constructor de la clase para inicializar los atributos
        self.name = name

    def saludo(self): # Metodo saludo, perteneciente  a la clase.
        print(f"Hello, {self.name} is this a class in python") #Mensaje personalizado

fabian = Person("Fabian") # Creaciòn de una instancia(Objeto) de la clase 'Person'

fabian.saludo() # Llamada al mètodo saludo