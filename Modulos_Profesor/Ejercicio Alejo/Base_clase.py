#La gobernación de Santander están organizando un evento deportivo en el cual se estarán organizando tres carreras:
#atletismo
#ciclismo
#patinaje
#Para esta organización la gobernación comenzó a recolectar la información de los participantes en planillas manualmente, sin esperar que habría demasiada gente interesada 
# y la cantidad de personas inscritas fue poco manejable. La gobernación requiere un programa simple hecho en Python que le permita recolectar la información de los participantes 
# con los siguientes requerimientos.

#La aplicación debe:
#Permitir registrar a los participantes mayores a 18 años y residentes en el departamento de Santander, pidiéndole seleccionar una de las tres carreras en la cual participar.
#Marcar en un ranking las 5 primeras posiciones a los participantes de cada carrera.
#No se permite la modificación de la información a los participantes.
#Mantener la información de los participantes registrados es decir que no finalice, solamente si el usuario lo indica.
#Puede tener menús y submenús tantos como se requiera siempre y cuando sea ordenado y entendible. Para finalizar la aplicación se debe pedir confirmación
#Tener una estructura organizada   a nivel de código con módulos y funciones.

def Registro_Participantes(data):
    print("-------------------------------------------------------")
    usuario = {}
    edad = int(input( " ingrese su edad--> "))
    departamento = input( " ingrese su deparetamento--> ")
    departamento.lower()
    if edad >= 18 and departamento == 'santander':
        cedula = input( " ingrese la cedula--> ")
        if data.get( cedula, None) == None:
            print("-------------------------------------------------------")
            print(" Participante no  registrado")
            print( 'ingrese los datos')
            usuario["Nombre"] = input( " ingrese el nombre--> ")
            usuario["Carrera"] = input( " Competencia-->")
            usuario['Edad'] = edad
            usuario['Departamento'] = departamento
            data[cedula] = usuario
            print("-------------------------------------------------------")
    else:
        print( 'No puede participar')
          
def ingresa_posicio(data):
     print("-------------------------------------------------------")
     usuario = {}
     cedula = input("Ingrese la cedula del participante--> ")
     if data.get( cedula, None ) == None:
        print( "usuario no existe debe registrarlo ")
     else:
        usuario["posicion"] = input( "ingrese su puesto en numero--> ")
        data[cedula] = usuario  
        

partipantes = {"1095824299":
                            {"Nombre": "Alejandro", "Edad":29, "Carrera": "atletismo ","posicion":100,  "Departamenbto":'santander' }
}


def menu ( partipantes):
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

    