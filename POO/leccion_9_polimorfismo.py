# Definiciòn del nombre de la clase
class Mascota:

    className = "Mascota"  # Atributo de la clase

    # Constructor dee la clase para inicializar los atributos
    def __init__(self, name, especie):
        self.name = name        # Atributo que almacena el nombre
        self.especie = especie  # Atributo que almacena la especie

    # Método público que imprime los datos de la mascota
    def print_data(self):
        print(f"The pet's name is {self.name} and it belongs to the species {self.especie}")

# Definición de la clase hija "Veterinaria" que hereda de "Mascota"
class Veterinaria(Mascota):

    # Constructor de la clase hija
    def __init__(self, name, especie, propietario):
        super().__init__(name, especie)  # Llama al constructor de la clase padre para inicializar "name" y "especie"
        self.propietario = propietario   # # Atributo propio de la clase hija que almacena la profesión

    # Sobrescritura (override) del método "saludo" de la clase padre
    def print_data(self):

        # Nueva implementación personalizada para la clase hija
        print(f"The {self.especie} is called {self.name} and his owner is {self.propietario}")

# Función global que recibe un objeto y llama al método "print_data"
# Esto es un claro ejemplo de polimorfismo, ya que acepta cualquier objeto que tenga ese método,
# sin importar si es de la clase padre o de la hija
def show(animal):
    animal.print_data() # Llamada al método correspondiente según la clase del objeto recibido

# Creación de instancias de las clases anteriores
gallo = Veterinaria("Gallo", "Ave", "Liam")  # Instancia de la clase hija
perro = Mascota("Torta", "Perro")            # Instancia de la clase padre

# Llamado de la función global "show", que aplica polimorfismo al ejecutar el método correcto según la clase
show(gallo)  # Llama al método sobreescrito en Veterinaria
show(perro)  # Llama al método original de Mascota