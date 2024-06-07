

def Registr_Participantes (data):
    print("-------------------------------------------------------")
    usuario = {}
    nombre = input("Ingrese su nombre--> ")
    telefono = input("ingrese su numero de telefono--> ")
    edad = int(input("ingrese su edad--> "))
    doc = input(" Ingrese su mumero de documento -- >")
    departamento = input("ingrese su departamento--> ") 
    departamento = departamento.lower()
    if data.get( doc, None ) == None:
        print("-------------------------------------------------------")
        print( "1 Para atletismo, 2 para ciclismo , para patinaje ")
        disiplina  = int(input( " ingrese el numero de la competencia que realizara-->"))
        if disiplina == 1:
            deporte= "Atletismo"
        elif disiplina == 2:
            deporte = "Ciclismo"
        
        elif disiplina == 3:
            deporte = "Patinaje"
        else:
            print("No Valido")
        if edad >= 18  and departamento == "santander":
            usuario["Nombre"]= nombre
            usuario["Edad"]= edad
            usuario["Telefono"]= telefono
            usuario["Departamento"]= departamento
            data[deporte][doc] = usuario
        else:
            print(" No puede competir")
    else:
        print("Usuario Registrado")
        
        
deportes = {
    "atletismo": {
        "1": {"Nombre": "Juan", "tel": 3221122222, "doc": "1545454"},
        "2": {"Nombre": "Alejandro", "tel": 3178876, "doc": "1095824299"},
    }
}  


menu = ( "1.Para Registrar", "2.Para ingresas posicion", "3.Para ver posiciones", "4.Para salir ")
#print(partipantes_ordenados)

while True:
    for i in menu:
        print(i)
    op = input(' Elija la opcion--> ')  
    if op == '1':
         Registr_Participantes(deportes)
    elif op == "2":
        break
  
        


    
    
    