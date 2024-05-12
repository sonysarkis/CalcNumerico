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

# Este método traduce los números que sean mayores a 9 a su correspondiente letra en hexadecimal
# Por ejemplo, el 10 que conocemos en decimal corresponde a la letra A en hexadecimal.
def traduccion_hexa(n, c):
    if c == 16:
        if n == 10: return "A"
        elif n == 11: return "B"
        elif n == 12: return "C"
        elif n == 13: return "D"
        elif n == 14: return "E"
        elif n == 15: return "F "
    return str(n)

# Método para convertir un número decimal a cualquier número con base c
# Esto toma cualquier número decimal y dependiendo del valor que le demos a C, nos trasformará 
# a esa base. Si c=8, nos dara un octal, si c=3, nos dara un terciario, y asi sucesivamente
def decimal_a_cualquiera(n,c):
    # n será el número decimal que queremos convertir a cualquier base c
    if n < 2: # Si el número es menor a 2, retornamos el número en string porque ya no se puede dividir más 
        return str(n)
    return decimal_a_cualquiera(n // c,c) + traduccion_hexa(n % c, c) # Este método se llama recursivamente hasta que n sea menor a 2
                                                       # Se divide n entre c y se obtiene el cociente y el residuo de la división
                                        # El residuo se traduce a su correspondiente letra en hexadecimal (en caso de ser mayor a 9) y se concatena con el cociente
                                                       


op = int(input("""
            Presione [1] para ingresar un número binario.
            Presione [2] para ingresar un número decimal.
            Presione [3] para ingresar un número terciario. 
            Presione [4] para ingresar un número cuaternario.
            Presione [5] para ingresar un número octal.
            Presione [6] para ingresar un número hexadecimal.
            Ingrese su opción numérica:   """))

if op == 1: # Binario a todas las bases  
    # Método para convertir de binario a decimal
    def todo_a_decimal(num,c=2): # Inicializamos c=2 para que el divisor sea 2 y así convertir de binario a decimal
        if len(num) == 1:
            return int(num)
        return c * todo_a_decimal(num[:-1]) + int(num[-1])
    
    # Método para validar que el número ingresado sea binario
    def validar_binario(num):
        for i in num:
            if i in ["0","1"]:
                return True
        return False
    
    numero_binario = input("Ingrese un número binario: ")
    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_binario} en terciario es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=3)}") 
    # Inicializamos c=4 para que 4 sea el divisor y poder obtener el número cuarternario 
    print(f"{numero_binario} en cuaternario es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=4)}")
    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_binario} en decimal es: {todo_a_decimal(numero_binario)}")
    # Inicializamos c=8 para que 8 sea el divisor y poder obtener el número octal
    print(f"{numero_binario} en octal es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=8)}")
    # Inicializamos c=16 para que 16 sea el divisor y poder obtener el número hexadecimal
    print(f"{numero_binario} en hexadecimal es: {decimal_a_cualquiera(todo_a_decimal(numero_binario),c=16)}")

if op == 2: # Decimal a todas las bases
    
    # Llamamos al método decimal_a_cualquiera ya definida para convertir a cualquier base
    numero_decimal = int(input("Ingrese un número decimal: "))
    # Inicializamos c=2 para que 2 sea el divisor y poder obtener el número binario
    print(f"{numero_decimal} en binario es: {decimal_a_cualquiera(numero_decimal, c=2)}")

    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_decimal} en terciario es: {decimal_a_cualquiera(numero_decimal, c=3)}")

    # Inicializamos c=4 para que 4 sea el divisor y poder obtener el número cuarternario
    print(f"{numero_decimal} en cuaternario es: {decimal_a_cualquiera(numero_decimal, c=4)}")

    # Inicializamos c=8 para que 8 sea el divisor y poder obtener el número octal
    print(f"{numero_decimal} en octal es: {decimal_a_cualquiera(numero_decimal, c=8)}")
    
    # Inicializamos c=16 para que 16 sea el divisor y poder obtener el número hexadecimal
    print(f"{numero_decimal} en hexadecimal es: {decimal_a_cualquiera(numero_decimal, c=16)}")

if op == 3: # Terciario a todas las bases
    # Método para validar que el número ingresado sea terciario
    def validar_terciario(num):
        for i in num:
            if i in ["0","1","2"]:
                return True
        return False
    
    # Método para convertir de terciario a decimal
    def todo_a_decimal(num,c=3): # Inicializamos c=3 porque queremos convertir de terciario a decimal
        if len(num) == 1:
            return int(num)
        return c * todo_a_decimal(num[:-1]) + int(num[-1])
    
    # Input del número terciario a convertir
    numero_terciario = input("Ingrese un número terciario: ")

    if validar_terciario(numero_terciario) != True:
        print("Número terciario inválido.")
        exit()
    # Inicializamos c=2 para que 2 sea el divisor y poder obtener el número binario
    print(f"{numero_terciario} en binario es: {decimal_a_cualquiera(todo_a_decimal(numero_terciario),c=2)}")
    # Inicializamos c=4 para que 4 sea el divisor y poder obtener el número cuarternario
    print(f"{numero_terciario} en cuaternario es: {decimal_a_cualquiera(todo_a_decimal(numero_terciario),c=4)}")
    # Aquí no inicializamos c porque ya el número está en terciario y queremos convertirlo a decimal
    print(f"{numero_terciario} en decimal es: {todo_a_decimal(numero_terciario)}")
    # Inicializamos c=8 para que 8 sea el divisor y poder obtener el número octal
    print(f"{numero_terciario} en octal es: {decimal_a_cualquiera(todo_a_decimal(numero_terciario),c=8)}")
    # Inicializamos c=16 para que 16 sea el divisor y poder obtener el número hexadecimal
    print(f"{numero_terciario} en hexadecimal es: {decimal_a_cualquiera(todo_a_decimal(numero_terciario),c=16)}")

if op == 4: # Cuaternario a todas las bases
    # Método para convertir de cuaternario a decimal
    def todo_a_decimal(num,c=4): # Inicializamos c=4 porque queremos convertir de cuaternario a decimal
        if len(num) == 1:
            return int(num)
        return c * todo_a_decimal(num[:-1]) + int(num[-1])
    
    # Método para validar que el número ingresado sea cuaternario
    def validar_cuaternario(num):
        for i in num:
            if i in ["0","1","2","3"]:
                return True
        return False
    
    # Input del número cuaternario a convertir
    numero_cuaternario = input("Ingrese un número cuaternario: ")
    # Inicializamos c=2 para que 2 sea el divisor y poder obtener el número binario
    print(f"{numero_cuaternario} en binario es: {decimal_a_cualquiera(todo_a_decimal(numero_cuaternario),c=2)}")
    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_cuaternario} en terciario es: {decimal_a_cualquiera(todo_a_decimal(numero_cuaternario),c=3)}")
    # Aquí no inicializamos c porque ya el número está cuaternario y queremos convertirlo a decimal
    print(f"{numero_cuaternario} en decimal es: {todo_a_decimal(numero_cuaternario)}")
    # Inicializamos c=8 para que 8 sea el divisor y poder obtener el número octal
    print(f"{numero_cuaternario} en octal es: {decimal_a_cualquiera(todo_a_decimal(numero_cuaternario),c=8)}")
    # Inicializamos c=16 para que 16 sea el divisor y poder obtener el número hexadecimal
    print(f"{numero_cuaternario} en hexadecimal es: {decimal_a_cualquiera(todo_a_decimal(numero_cuaternario),c=16)}")

if op == 5: # Octal a todas las bases

    def OctalBinario(n):
        try:
            octal = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
            bin = str(''.join(octal[num] for num in n)) # Itera sobre cada dígito num en el número 
                                                        #octal n, y para cada dígito se busca su 
                                                        #representación en binario en el diccionario octal. 
                                                        #El resultado se concatena en una cadena bin.
            return bin.lstrip('0') # lstript('0') elimina los ceros innecesarios a la izquierda
        except:
            raise "ERROR. Número octal inválido."
    
    # Método para convertir de octal a decimal
    def todo_a_decimal(num,c=8): # Inicializamos c=8 porque queremos convertir de octal a decimal
        if len(num) == 1:
            return int(num)
        return c * todo_a_decimal(num[:-1]) + int(num[-1])
    
    # Input del número octal a convertir
    numero_octal = input("Ingrese un número octal: ")

    # Inicializamos c=2 para que 2 sea el divisor y poder obtener el número binario
    print(f"{numero_octal} en binario es: {decimal_a_cualquiera(todo_a_decimal(OctalBinario(numero_octal)),c=2)}")

    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_octal} en terciario es: {decimal_a_cualquiera(todo_a_decimal(numero_octal),c=3)}")

    # Inicializamos c=4 para que 4 sea el divisor y poder obtener el número cuarternario
    print(f"{numero_octal} en cuaternario es: {decimal_a_cualquiera(todo_a_decimal(numero_octal),c=4)}")

    # Aquí no inicializamos c porque ya el número está en octal y queremos convertirlo a decimal
    print(f"{numero_octal} en decimal es: {todo_a_decimal(numero_octal)}")

    # Inicializamos c=16 para que 16 sea el divisor y poder obtener el número hexadecimal
    print(f"{numero_octal} en hexadecimal es: {decimal_a_cualquiera(todo_a_decimal(numero_octal),c=16)}")

if op == 6: # Hexadecimal a todas las bases

    # Método para convertir de hexadecimal a decimal
    def todo_a_decimal(num,c=16):
        num = num.upper() # .upper() convierte las letras a mayúsculas para evitar errores al traducir a hexadecimal 
        if len(num) == 1:
            return int(num,c)
        return c * todo_a_decimal(num[:-1]) + int(num[-1],c) # 
    
    # Input del número hexadecimal a convertir
    numero_hexadecimal = input("Ingrese un número hexadecimal: ")
    # Inicializamos c=2 para que 2 sea el divisor y poder obtener el número binario
    print(f"{numero_hexadecimal} en binario es: {decimal_a_cualquiera(todo_a_decimal(numero_hexadecimal),c=2)}")
    # Inicializamos c=3 para que 3 sea el divisor y poder obtener el número terciario
    print(f"{numero_hexadecimal} en terciario es: {decimal_a_cualquiera(todo_a_decimal(numero_hexadecimal),c=3)}")
    # Inicializamos c=4 para que 4 sea el divisor y poder obtener el número cuarternario
    print(f"{numero_hexadecimal} en cuaternario es: {decimal_a_cualquiera(todo_a_decimal(numero_hexadecimal),c=4)}")
    # Inicializamos c=8 para que 8 sea el divisor y poder obtener el número octal
    print(f"{numero_hexadecimal} en octal es: {decimal_a_cualquiera(todo_a_decimal(numero_hexadecimal),c=8)}")
    # Aquí no inicializamos c porque ya el número está en hexadecimal y queremos convertirlo a decimal
    print(f"{numero_hexadecimal} en decimal es: {todo_a_decimal(numero_hexadecimal)}")

