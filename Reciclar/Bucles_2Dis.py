#2. Escribir un programa que pregunte al usuario su edad y
# muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int (input( 'ingrese su edad '))

for i in range ( 0,edad,1):
    print( ' en el ano', 2024 - i , 'tienes'   ,  edad -i ) 
    