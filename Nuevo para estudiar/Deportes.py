
def Regisatro_Deporte (data):
     posicion = int(input("Ingrese su posicion: "))
     deporte = input("Ingrese su deporte (Atletismo - Ciclismo - Patinaje): ")
     doc = input("Ingrese su documento: ")
     
     if deporte not in data:
        data[deporte] = {}
        
     if posicion not in data[deporte]:
        data[deporte][posicion] = {}
    # Verifica si la posición existe en el diccionario del deporte, si no, lo crea
     if posicion not in data[deporte]:
        data[deporte][posicion] = {}
        
    # Verifica si el documento ya está registrado en esa posición y deporte
     if doc not in data[deporte][posicion]:
        nombre = input("Ingrese su Nombre: ")
        edad = int(input("Ingrese su Edad: "))
        # Guarda los datos del usuario en el diccionario
        data[deporte][posicion][doc] = {"Nombre": nombre, "Edad": edad}
     else:
        print("El documento ya está registrado en esa posición y deporte.")
    
   
     


Deportes = { "Atletismo" : { '1':{"Nombre":"Alejandro", "Edad": 29},
                            '10':{"Nombre":"Jhoan", "Edad": 27},
                             '2': { "Nombre":"Camila", "Edad": 25}
}
}  
            
print ("Bienvenido al sistema de ingreso")
print("felicidades por terminar tu carrera ingresa tus datos")

print( "Eres de Santander  ? 1. SI  2. NO  ")
santander = input("--->  ")
if santander =='1':
    print( "Eres mayor de edad ? ingresa tu edad ")
    edad = int ( input("--->"))
    if edad <= 18: 
        print( "No Puede participar")
    else:
       
        
        while True:
            print('MENU')
            menu = ("1. Para registrar sus datos","2. Para ver el ranking ", "3. Para ver todos los usuarion presentaods", "4. Salir ")
            print(menu)
            op  = input( "--->")
            if op == "1":
                Regisatro_Deporte (Deportes)

                
            
            if op =='2':
                for llave, valor in Deportes.items():
                    print(valor,llave)
                    
            

            #elif op == 3:
            
            elif op == "4": 
                print( " Saliendo del sistema")    
                break
else:
    print("No puede ingresar sus datos ")
        
    


          
      


