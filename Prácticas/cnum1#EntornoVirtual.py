# Clase persona con "nombre, edad, dni" como atributos
class Persona:
    def __init__(self, nombre, edad, dni) :
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Getters para recuperar los datos atributos    
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad 

    def getDni(self):
        return self.dni

    # Mostrar datos recuperados 
    def mostrarDatos(self):
        print("Nombre:",self.nombre,"\n",
              "Edad:",self.edad,"años","\n", 
              "DNI:",self.dni,"\n")

    # Método para verificar si la persona es mayor de edad o no
    def mayor(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} no es mayor de edad")   


# Crearemos una clase para generar una lista, para trabajar con varios objetos en vez de uno solo.
class generarPers():
    listaPersonas = []
    def __init__(self, lista):
        self.listaPersonas = lista

    # Creamos una funcion para la lista diciendo quien es mayor y quien no.
    def mostrarLista(self):
        for Persona in self.listaPersonas:
            if Persona.mayor():
                Persona.getNombre()

# Creamos objeto
conjuntoPers = generarPers([
    Persona("Sony", 19, 31276865),
    Persona("Alex", 16, 16276595),
    Persona("Alejandro", 24, 25768565),
    Persona("Mario", 13, 19257368),
    Persona("Carolina", 29, 17968565)

])
# Mostramos la lista 
conjuntoPers.mostrarLista()
