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