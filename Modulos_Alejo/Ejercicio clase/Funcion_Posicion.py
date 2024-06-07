def ingresa_posicio(data):
     print("-------------------------------------------------------")
     usuario = {}
     cedula = input("Ingrese la cedula del participante--> ")
     if data.get( cedula, None ) == None:
        print( "usuario no existe debe registrarlo ")
     else:
        usuario["posicion"] = input( "ingrese su puesto en numero--> ")
        
        
        
        
        
        
        data[cedula] = usuario 