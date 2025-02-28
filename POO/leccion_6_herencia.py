class Movies: # Definiciòn del nombre de la clase
    className = "Movies" # Atributo de clase

    # Constructor de la clase para inicializar los atributos de la instancia
    def __init__(self, name: str, year: int):
        self.name = name    # Atributo pùblico que almacena el nombre de la película
        self.year = year    # Atributo pùblico que almacena el año de la película

    def print_data_movie(self): # Mètodo público de la isntancia para que imprime mensaje
        print(f"Hello, the name of movie is {self.name} from year {self.year}.")



class Cine(Movies): # Definiciòn de una clase que hereda de la clase 'Movies'.
    pass            # Herendar el constructor de la primera clase.

    className = "Primera toma" # Atributo de clase

    # Mètodo pùblico de instancia para imprimir un mensaje haciendo uso de los atributos de la clase padre
    def mensaje(self):
        print(f"Hello, welcome to {self.className}, today we have the movie {self.name} from year {self.year} "
              f"at 7:00 pm")

# Creaciòn de la instacia de la clase 'Cine'
funcion = Cine("Avatar", 2000)
funcion.mensaje()  # LLamar al mètodo de 'mensaje' que hereda atributos de la clase padre.


