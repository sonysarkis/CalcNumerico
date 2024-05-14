"""
Desarrolla una función en Python que implemente el método de Gauss-Seidel para resolver un 
sistema de ecuaciones lineales de la forma Ax = b, donde A es una matriz cuadrada de tamaño nxn, 
b es un vector de tamaño n, y x es el vector de incógnitas que queremos encontrar. La función debe 
tomar como entrada la matriz A, el vector b, un vector inicial x0 (puede ser un vector de ceros) y 
opcionalmente la tolerancia y el número máximo de iteraciones. La función debe devolver el vector x 
que resuelve el sistema de ecuaciones lineales.



SOLO BACKEND, NO FRONTEND
"""

import numpy as np
import numpy as np 

A = np.array([[3, -0.2, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
b = np.array([7.85, -19.3, 71.4])

x1 = 0
x2 = 0
x3 = 0
contador_iteraciones = 0

aux1 = x1
x1 = (b[0] - A[0][1]*x2 - A[0,2]*x3)/A[0,0]
x2 = (b[1]- A[1][0]*x1 - A[1][2]*x3)/ A[1][1]
x3 = (b[2]- A[2][0]*x1 - A[2][1]*x2)/ A[2][2]
error = abs(x1-aux1/x1)

while True:
    aux1 = x1
    x1 = (b[0] - A[0][1]*x2 - A[0,2]*x3)/A[0,0]
    x2 = (b[1]- A[1][0]*x1 - A[1][2]*x3)/ A[1][1]
    x3 = (b[2]- A[2][0]*x1 - A[2][1]*x2)/ A[2][2]
    error = abs(x1-aux1/x1)
    contador_iteraciones += 1
    if error < 0.0001:
        break
    if contador_iteraciones == 1000:
        break




print(x1, x2, x3) 
print("Solución encontrada en: ", contador_iteraciones, "iteraciones") 