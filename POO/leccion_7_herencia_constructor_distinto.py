class Movies: # Definiciòn del nombre de la clase
    className = "Movies" # Atributo de clase

    # Constructor de la clase para inicializar los atributos de la instancia
    def __init__(self, name: str, year: int):
        self.name = name    # Atributo pùblico que almacena el nombre de la película
        self.year = year    # Atributo pùblico que almacena el año de la película

    def print_data_movie(self): # Mètodo público de la isntancia para que imprime mensaje
        print(f"Hello, the name of movie is {self.name} from year {self.year}.")

# definiciòn de la clase hija que hereda de Movies
class Critica(Movies): # Se define la herencia añadiendo la relacion entre la clase hija y la padre.

    # Definiciòn del constructor de la case hija
    def __init__(self, name, year, name_critico):
        # Lamada del constructor de la clase padre para inicializar los atributos
        super().__init__(name, year) # Hereda e inicializa los atributos "name" y "year"

        # Atributo propio de la clase "Critica"
        self.name_critico = name_critico

# Creación de una instancia de la clase hija 'Critica'
maquivelo = Critica("Once Upon a Time in Hollywood", 2019, "Maquiavelo")

# Impresión del atributo propio de la clase hija
print(maquivelo.name_critico)  # Salida: Maquiavelo

# Uso del método heredado de la clase padre 'Movies'
maquivelo.print_data_movie()  # Salida: Hello, the name of movie is Once Upon a Time in Hollywood from year 2019.
