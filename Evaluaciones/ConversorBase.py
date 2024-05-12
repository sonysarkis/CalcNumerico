# Método para convertir cualquier número con su base a número con base decimal (10)
def todo_a_decimal(num,c):
        # Cuando usemos este método, inicializamos c=2 si queremos convertir de número binario a número decimal
        # Inicializamos c=3 si queremos convertir de terciario a decimal, y asi sucesivamente.
        if len(num) == 1:
            # Si la longitud del número es 1, retornamos el número en entero
            return int(num)
        return c * todo_a_decimal(num[:-1]) + int(num[-1]) #  num[:-1] es el número sin el último dígito y num[-1] es el último dígito
                                                           #  este método se llama recursivamente hasta que la longitud del número sea 1
                                                           #  se multiplica el número sin el último dígito por la base y se suma el último dígito para obtener el número en decimal


# Método para convertir un número decimal a cualquier número con base c
def decimal_a_cualquiera(n,c):
    # n será el número decimal que queremos convertir a cualquier base c
    if n < 2: # Si el número es menor a 2, retornamos el número en string porque ya no se puede dividir más 
        return str(n)
    return decimal_a_cualquiera(n // c,c) + str(n % c) # Este método se llama recursivamente hasta que n sea menor a 2
                                                       # Se divide n entre c y se obtiene el cociente y el residuo de la división
                                                       # Se concatena el residuo a la cadena que se va formando
                                                       # 

op = int(input("""
            Presione [1] para ingresar un número binario.
            Ingrese su opción numérica:   """))

if op == 1:     
    # Método para convertir de binario a decimal
    def todo_a_decimal(num,c=2): # Inicializamos c en 2 para convertir binario a decimal, c siendo el divisor
        if len(num) == 1:
            return int(num)
        return c * todo_a_decimal(num[:-1]) + int(num[-1])
    
     # Esto toma cualquier numero decimal y dependiendo del valor que le demos a C, nos trasformará 
     # A esa base. Si c=8, nos dara un octal, si c=3, nos dara un terciario, y asi sucesivamente
    def decimal_a_cualquiera(n,c):
        if n < 2:
            return str(n)
        return decimal_a_cualquiera(n // c,c) + str(n % c)
     
    numero_binario = input("Ingrese un número binario: ")
    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_binario} en terciario es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=3)}") 
    # Inicializamos c=4 para que 4 sea el divisor y poder obtener el número cuarternario 
    print(f"{numero_binario} en cuarternario es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=4)}")
    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_binario} en decimal es: {todo_a_decimal(numero_binario)}")
    # Inicializamos c=8 para que 8 sea el divisor y poder obtener el número octal
    print(f"{numero_binario} en octal es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=8)}")
    # Inicializamos c=16 para que 16 sea el divisor y poder obtener el número hexadecimal
    print(f"{numero_binario} en hexa es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=16)}")
