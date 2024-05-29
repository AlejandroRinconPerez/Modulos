from Funcion_Registro import*
from Funcion_Posicion import*




def menu ( partipantes,op):
    menu = ( "1 Para Registrar", "2 Para ingresas posicion", "3. Para salir ")

    while True:
        for i in menu:
            print(i)
        op = input(' Elija la opcion--> ')  
        if op == '1':
            Registro_Participantes(partipantes)
        elif op == '2':
            ingresa_posicio(partipantes)
        elif op == '3':
            print("------Salir del sistema-------")
            break 