from Funcion_Registro import*
from Funcion_Posicion import*


partipantes = {"1095824299":
                            {"Nombre": "Alejandro", "Edad":29, "Carrera": "atletismo ","posicion":100,  "Departamenbto":'santander' }
}
menu = ( "1 Para Registrar", "2 Para ingresas posicion", "3. Para salir ")

def menu ():
    for i in menu:
            print(i)
    print(" Seleccione--> ")
    op = input(' Elija la opcion--> ')
    return op 


def menuprincipal():
    
    op = menu ()
    while True:
        if op == '1':
            Registro_Participantes(partipantes)
        elif op == '2':
            ingresa_posicio(partipantes)
        elif op == '3':
            print("------Salir del sistema-------")
            break 