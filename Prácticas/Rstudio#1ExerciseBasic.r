# Pedimos nombre y apellido al usuario
nombre <- readline(prompt =paste("Ingrese su primer nombre: "))
apellido <- readline(prompt = paste("Ingrese su primer apellido: "))

# Entrada de números
num1 <- as.integer(readline(prompt=paste("¡Efectuemos una multiplicación! Ingresa un número: ")))
num2 <- as.integer(readline(prompt=paste("Ingresa otro número: ")))

# Almacenamos resultado en una variable
resultado <- num1 * num2

# Mostramos el saludo y su operación arimética
print(paste("Hola", nombre, apellido,"¡Un gusto saludarle! El resultado de su multiplicación es:", resultado))