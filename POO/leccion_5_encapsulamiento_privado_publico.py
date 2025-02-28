
class Movies: # Definiciòn del nombre de la clase
    className = "Movies" # Atributo de clase

    # Constructor de la clase para inicializar los atributos de la instancia
    def __init__(self, name: str, year: int):
        self.name = name    # Atributo pùblico que almacena el nombre de la película
        self.__year = year  # Atributo privado que almacena el año de la película


    def get_year(self): # Mètodo público de la isntancia para poder acceder al atributo privado
        return self.__year # Retorna el dato del atributo privado

    def print_data_movie(self): # Mètodo público de la isntancia para que imprime mensaje
        print(f"Hello, the name of movie is {self.name} from year {self.get_year()}.")
        # Uso del mètodo "self.get_year()" para al atributo privado.

    def __saludo(self): # Mètodo privado de la isntacia
        print("Hello, is this mesaje from method private")

# Creaciòn de una isntancia de la clase 'Movies'
cars = Movies("Cars", 2009)
cars.print_data_movie()  # Llamar al metodo de la isntancia

print(cars.name)      # Imprimir atributio público
print(cars.get_year()) # Imprimir atributo privado haciendo uso del metodo "get_year()"

# cars.__saludo()  # Esto generará un error porque el método es privado

# Forma no recomendada pero posible de acceder al método privado
cars._Movies__saludo()