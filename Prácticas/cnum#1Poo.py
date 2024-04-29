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


# Creamos el objeto y le asignamos los valores
person1 = Persona("Alejandra", 19, "31268878")
person1.mostrarDatos()
person1.mayor()
