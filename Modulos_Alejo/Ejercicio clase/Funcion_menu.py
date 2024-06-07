from Funcion_Posicion import*
from Funcion_Registro import*
from Data import*

menu = ( "1 Para Registrar", "2 Para ingresas posicion", "3. Para ver posiciones", "4. Para salir ")

def menu ( ):
    menu = ( "1 Para Registrar", "2 Para ingresas posicion", "3. Para ver posiciones", "4. Para salir ")

    for i in menu:
        print(i)
    op = input(' Elija la opcion--> ')  
    return op

def submenu():
    while True:
        op=menu()
        if op == '1':
            Registro_Participantes(partipantes)
        elif op == '2':
            ingresa_posicio(partipantes)

        #elif op == '3':
            #ranking(partipantes)

        elif op == '4':
            print("------Salir del sistema-------")
            break 
