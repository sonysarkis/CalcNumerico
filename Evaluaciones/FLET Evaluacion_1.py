"""Interfaz usando flet donde el usuario ingrese aleatoriamente una matriz nxn y un vector de nx1
y se le devuelva el resultado de aplicar el método de Gauss Seidel
"""

# Realizado en un entorno virtual usando python 3.12.3

import flet as ft
from flet import *
import numpy as np

# Funcion principal 
def main(page: ft.Page):
    page.title = "Sony Gómez - Proyecto 1"
    page.theme_mode = ft.ThemeMode.LIGHT
    titulo = ft.Text("                                                                                                GAUSS SEIDEL", style=ft.TextStyle(size=20))
   
    
    # Input matriz nxn y el vector nx1 en un campo de texto
    label_matriz = ft.TextField(label="Ingrese la matriz NXN (elementos separados por comas y filas separadas por punto y coma):")
    label_vector = ft.TextField(label="Ingrese el vector NX1 (elementos por comas:")
    # Aqui se almacenará el resultado 
    result = ft.Text()


    ################################# MÉTODO VALIDACIONES#################################
    
    # Método que limpia todo el contenido de los campos de texto
    def limpiar():
        label_matriz.value = ""
        label_vector.value = ""
        result.value = ""
        page.update()

    # Método que rellena aleatoriamente la matriz y el vector siguiendo el formato solicitado
    def llenar_aleatorio():
        # Generar la matriz aleatoria
        matriz = np.random.randint(1, 10, (3, 3)) # Generar una matriz de 3x3 con números aleatorios entre 1 y 9
        matriz = matriz.tolist() # Convertir la matriz a lista
        matriz = ";".join([",".join(map(str, fila)) for fila in matriz]) # Formatear la matriz
        label_matriz.value = matriz # Mostrar la matriz en el campo de texto
        
        # Generar el vector aleatorio
        vector = np.random.randint(1, 9, 3) # Generar un vector de 3 elementos con números aleatorios entre 1 y 9
        vector = ",".join(map(str, vector)) # Formatear el vector
        label_vector.value = vector # Mostrar el vector en el campo de 
        page.update()


#################################Validaciones#################################
    
    # Método para validar que no se ingrese letra ni floats en la matriz
    def validaEntrada(matriz):
        try:
            for fila in matriz.split(";"):
                for elemento in fila.split(","):
                    int(elemento)
            return True
        except:
            return False
        
    # Método para validar que la matriz sea cuadrada
    def validaMCuadrada(matriz):
        filas = matriz.split(";")
        elementos = [elemento.split(",") for elemento in filas]
        numfilas = len(filas) # Número de filas de la matriz 
        for fila in elementos:
            if len(fila) != numfilas: # Si el número de elementos de una fila no es igual al número de filas, la matriz no es cuadrada
                return False
        return True
    
    # Método para validar que el vector sea de la misma longitud que la matriz
    def validaVector(matriz, vector):
        filas = matriz.split(";")
        elementos = [elemento.split(",") for elemento in filas]
        if len(elementos) != len(vector.split(",")):
            return False
        return True
    
    
    #################################FORMATEO MATRIZ Y VECTOR INGRESADO #################################

    # Metodo para procesar la matriz, vector ingresado y mostrarlo formateado
    def formatearMatriz():
        # Validamos que la matriz y el vector no estén vacíos
        if not label_matriz.value or not label_vector.value: # Not significa que si no hay nada en la matriz o en el vector, se muestre el mensaje
            result.value = "Falta información. Intente de nuevo."
            page.update()
            return
        
        # Validamos que la matriz y el vector sean enteros
        if validaEntrada(label_matriz.value)  == False or validaEntrada(label_vector.value) == False:
            result.value = "No se admiten letras ni números flotantes. Ingrese solo números enteros.\nNOTA: Si no ingresó letras o números flotantes, verifique el formato y compruebe si es el mismo que se solicitó."
            page.update()
            return
        
        # Validamos que la matriz sea cuadrada
        if not validaMCuadrada(label_matriz.value): # Not es una negación, si la matriz no es cuadrada, se muestra el mensaje
            result.value = "Error. La matriz debe ser cuadrada. Intente de nuevo"
            page.update()
            return
        
        # Validamos que el vector sea de la misma longitud que la matriz
        if validaVector(label_matriz.value, label_vector.value) == False:
            result.value = "Error. El vector debe tener la misma longitud que la matriz. Intente de nuevo"
            page.update()
            return
        
    
        # Ya pasada las validaciones, se procede a procesar la matriz y el vector
        obtener_matriz = label_matriz.value # Obtener la matriz ingresada por el usuario
        filas = obtener_matriz.split(";") # Separar las filas
        matriz = [elemento.split(",") for elemento in filas] # Separar los elementos de cada fila

        obtener_vector = label_vector.value # Obtener el vector ingresado por el usuario
        vector = obtener_vector.split(",") # Separar los elementos del vector
        vectorFinal = "Vector B (nx1):\n" + "\n".join(vector)  # Concatenamos y mostramos


        matrizFinal = "" # Inicializamos en nada para luego guardar allí la matriz formateada
        for elemento in matriz: # Recorremos las filas de la matriz
            elemento_fin = " ".join(elemento)  # Unir los elementos de la fila separados por coma
            matrizFinal += elemento_fin + "\n"  # Agregamos la fila al texto de la matriz

        
 #################################Convertir la matriz y el vector a numpy array#################################
         # Convertir la matriz y el vector a arreglos numpy 
        matriz_numpy = np.array(matriz, dtype=int) # dtype= int significa que los elementos de la matriz serán enteros 
        vector_numpy = np.array(vector, dtype=int)
        A = matriz_numpy.tolist() # Convertimos la matriz a lista y esta variable la usaremos para el método GaussSeidel
        b = vector_numpy.tolist() # lo mismo con el vector

       
                    #################################Gauss Seidel#################################

        # Creamos un vector que tenga tantos ceros como elementos tenga el vector b
        def gaussSeidel(a,b,x0 = None, error=0.000001, max_iteracion = 1000):
            n = len(b) # Obtenemos la longitud del vector b 
            x0 = np.zeros(n) # Inicializamos x0 = 0
            x = x0.copy() # Copiamos x0 a x para no modificar x0 porque lo necesitamos para comparar el error
            for k in range(max_iteracion): # Que se repita hasta que se cumpla la condición en un máximo de 1000 iteraciones
                for i in range(n):
                    # np.dot multiplica los elementos de dos arreglos y los suma 
                    # se usa np.dot(a[i][:i], x[:i]) para multiplicar los elementos de la fila i de la matriz a con los elementos de x que están antes de la posición i
                    # se usa np.dot(a[i][i+1:], x[i+1:]) para multiplicar los elementos de la fila i de la matriz a con los elementos de x que están después de la posición i
                    # se usa le restamos a b[i] la multiplicación calculada anteriormente
                    x[i] = (b[i] - np.dot(a[i][:i], x[:i]) - np.dot(a[i][i+1:], x[i+1:])) / a[i][i] # Aplicamos la fórmula de Gauss-Seidel
                if np.linalg.norm(x-x0) < error: # np.linalg.norm calcula la norma (norma = número no negativo) de un vector y si es menor al error, se rompe el ciclo. 
                    break
                x0 = x.copy() # Copiamos x en x0 para que en la siguiente iteración se compare con el valor anterior hasta cumplir la condición
            return x.tolist(), k+1 # Vector resultante y el número de iteraciones que se hicieron
        
        
        # Mostrar la matriz y el vector convertidos a arreglos numpy
        matrizFinal = "Matriz cuadrada (nxn):\n" + str(matriz_numpy)
        vectorFinal = "Vector b (nx1):\n" + str(vector_numpy)
        result.value = matrizFinal + "\n\n" + vectorFinal
        # Mostramos resultado de Gauss-Seidel
        x, iteraciones = gaussSeidel(A,b) # decimos que x y las iteraciones tendrán los valores que retorne la función en ese orden
        
        # Si el resultado son NAN o INF, se muestra un mensaje de error
        if np.isnan(x).any() or np.isinf(x).any():
            result.value += "\n\nError. El resultado contiene valores NAN (valor especial no representable) o INF (infinito)\nIntente de nuevo con otra matriz y vector."
            page.update()
            return
        result.value += f"\n\nVector resultante: {x}\nEl vector resultante fue encontrado en {iteraciones} iteraciones"
        page.update()

        

    #################################BOTONES#################################
    # Boton que hace la acción 
    Button_procesar = ft.ElevatedButton( 
        text="Procesar matriz y vector", 
        on_click=lambda _: formatearMatriz()
    )

    # Boton para limpiar los campos de texto
    Button_limpiar = ft.ElevatedButton(
        text="Limpiar todo",
        on_click=lambda _: limpiar())

    
    # Boton para llenar aleatoriamente la matriz y el vector
    Button_aleatorio = ft.ElevatedButton(
        text="Llenar aleatoriamente (Matriz 3x3 con números entre 1 y 9)",
        on_click=lambda _: llenar_aleatorio())
    
    
    # Añadimos elementos a la página
    page.add(titulo, label_matriz, label_vector,  Button_procesar, Button_aleatorio,Button_limpiar,result)
    
   

# Corre el programa
ft.app(target=main)