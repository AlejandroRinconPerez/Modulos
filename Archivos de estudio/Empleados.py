# 1. Una empresa requiere un sistema para controlar el ingreso de los empleados diariamente a la empresa. Para esto se requiere un menú con las siguientes funcionalidades:
# Registrar empleado
# Listar todos los empleados
# Modificar empleados
# Despedir empleados (Esta función no elimina al empleados solo cambia su estado)
# Registrar entrada empleados
# Registrar salida de empleados

from Datos_empleados import* 




def registro_empleados ():
    print("--------------------------------------------")
    Empleados = cargar_datos_Empleados()
    Registro_Info = {}
    Empleado = {}
    doc = input("Ingrese si cedula como Id unico")
    
    for Empleado in Empleados:
        if doc in Empleado:
            print(" Empleado existe")
            return
    Registro_Info["Nombre"] = input(" Ingrese su nombre:  ")
    Registro_Info["Apellido"] = input(" Ingrese su Apellido:  ")
    Registro_Info["Telefono"] = input(" Ingrese su Telefono:  ")
    Registro_Info["Cargo"] = input(" Ingrese su Cargo:  ")
    Empleado[doc]= Registro_Info
    Empleados.append(Empleado)
    guardar_datos_Empleados(Empleados)
    print("--------------------------------------------")
    return
    
    


def registro_Entrada ( ): 
    print("--------------------------------------------")
    Empleados = cargar_datos_Empleados()
    doc = input("Ingrese si cedula como Id unico")
    Registro = {}
    Registro["ano"] = int(input("Ingrese el ano en que estamos"))
    Registro["mes"] = int(input(" Ingrese el numero de mes "))
    Registro["dia"] = int( input("ingrese el dia "))
    fecha = f"{Registro["dia"]:02d}/{Registro["mes"]:02d}/{Registro["ano"]}"
    Registro[fecha] = {}
    hora_entrada = input("ingrese la hora de entrada")
    
    for Empleado in Empleados:
        if doc in Empleado:
            Empleado[doc]["fecha"]={}
            if fecha not in Empleado[doc]["fecha"]:
                Empleado[doc]["fecha"][fecha] ={}
            Empleado[doc]["fecha"][fecha]["Entrada"]= hora_entrada
            guardar_datos_Empleados(Empleados)
            print("--------------------------------------------")
            return
    else: print("Doc no encontrado")
    print("--------------------------------------------")
    return

def registro_Salida ( ): 
    print("--------------------------------------------")
    Empleados = cargar_datos_Empleados()
    doc = input("Ingrese si cedula como Id unico")
    Registro = {}
    Registro["ano"] = int(input("Ingrese el ano en que estamos"))
    Registro["mes"] = int(input(" Ingrese el numero de mes "))
    Registro["dia"] = int( input("ingrese el dia "))
    fecha = f"{Registro["dia"]:02d}/{Registro["mes"]:02d}/{Registro["ano"]}"
    Registro[fecha] = {}
    hora_Salida = input("ingrese la hora de Salida")
    
    for Empleado in Empleados:
        if doc in Empleado:
            if "fecha" not in Empleado[doc]:
                Empleado[doc]["fecha"]={}
            if fecha not in Empleado[doc]["fecha"]:
                Empleado[doc]["fecha"][fecha] ={}
            Empleado[doc]["fecha"][fecha]["Salida"]= hora_Salida
            guardar_datos_Empleados(Empleados)
            print("--------------------------------------------")
            return
    else: print("Doc no encontrado")
    print("--------------------------------------------")
    return
        
        
def lista_empleados ():
    print("--------------------------------------------")
    Empleados = cargar_datos_Empleados()
    print("Lista de empleados por nombre he Cargo")
    for Empleado in Empleados:
        for doc,datos in Empleado.items():
            print(f"Nombre {datos["Nombre"]} con el cargo {datos["Cargo"]} ")
            print("--------------------------------------------")
            
            
                
def agregar_estado ():
    print("--------------------------------------------")
    Empleados = cargar_datos_Empleados()
    doc = input("Agregue el documento")
    for Empleado in Empleados:
        if doc in Empleado:
            if "Estado" not in Empleado[doc]:
                nuevo_estado = input("Ingres el estado del empleado")
                Empleado[doc]["Estado"] = nuevo_estado
            nuevo_estado = input("Ingres el estado del empleado")
            Empleado[doc]["Estado"] = nuevo_estado
            guardar_datos_Empleados(Empleados)
            print("--------------------------------------------")
            return
            
    print("Doc no encontrado intente de nuevo")
    print("--------------------------------------------")
    return
def modificaciono_empleados ():
    print("--------------------------------------------")
    Empleados = cargar_datos_Empleados()
    Registro_Info = {}
    Empleado = {}
    doc = input("Ingrese si cedula como Id unico")
    
    for Empleado in Empleados:
        if doc in  Empleado:
            Registro_Info["Nombre"] = input(" Ingrese su nombre:  ")
            Registro_Info["Apellido"] = input(" Ingrese su Apellido:  ")
            Registro_Info["Telefono"] = input(" Ingrese su Telefono:  ")
            Registro_Info["Cargo"] = input(" Ingrese su Cargo:  ")
            Empleado[doc]= Registro_Info
            Empleados.append(Empleado)
            guardar_datos_Empleados(Empleados)
            print("--------------------------------------------")
            return
    print(" El empoleado no esta trabanado ")
    
def Empleado_Hora_fecha():
    Empleados = cargar_datos_Empleados()
    for Empleado in Empleados:
        for doc, datos in Empleado.items():
            if "fecha" in datos:
                print(f"El empleado {datos["Nombre"]} tiene el sigueinte registro de asistencia{datos["fecha"]}")
    
    return





#Empleado_Hora_fecha()
    
    
    
    
    
    
    
Menu = ("1. Registrar empleado", "2. Cambiar estado de empleado", "3. Hora de entrada", "4. Hora salida", "5. Salir")

# while True:
#     for i in Menu:
#         print(i)
#     op = int (input(" Opcion:   "))
#     if op == 1:
#         registro_empleados ()
#     if op == 2:
#         agregar_estado()
#     if op == 3:
#         registro_Entrada ( )
#     if op == 4:
#         registro_Salida()
#     if op == 5: 
#         break 
#     else:
#         print(" no valido")
        

        
        
# modificaciono_empleados ()





            

        


        

    

    

    

    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

