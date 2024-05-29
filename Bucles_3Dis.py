#4. Escribir un programa que pida al usuario un número entero positivo \
    # y muestre por pantalla la cuenta atrás desde ese número hasta cero.
    
    
num =  int(input( ' ingrese un numero cualquiera '))
print(num)
contador = 0

if num < 0:
    print( ' numero no valido debe ser positivo')
else:   
     for i in range ( num, 0 ,-1):
         print (num -1 )
         num = num -1 
         
        
          
