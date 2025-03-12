
class Person: #Definiciòn del nombre de la clase.

    def __init__(self, name): #Constructor de la clase para inicializar los atributos
        self.name = name # Atributo público que almacena el nombre de la persona

    # Método saludo, perteneciente a la clase "Person"
    def saludo(self): # Metodo saludo, perteneciente  a la clase "Person".
        print(f"Hello, {self.name} is this a class in python") #Mensaje personalizado


# Definiciòn de clase hija que hereda de la clase "Person"
class Profesion(Person): # "Profesion" hereda atributos y métodos de "Person"

    def __init__(self, name, profesion):
        super().__init__(name)     # Llama al constructor de la clase padre para inicializar "name"
        self.profesion = profesion # Atributo propio de la clase hija que almacena la profesión

    # Sobrescritura (override) del método "saludo" de la clase padre
    def saludo(self):
        # Nueva implementación personalizada para la clase hija
        print(f"Hello, my name is {self.name}. I'm {self.profesion}")

# Instancia de la clase hija
fabian = Profesion("Fabian", "Developer")
fabian.saludo() # Llamado del mètodo de la clase hija.