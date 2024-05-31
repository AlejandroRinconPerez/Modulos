
def Registro_de_Datos (data):
    Utilizado ={}
    print("Premium Plus y Normal")
    Plan_Utilizado = input("Ingrese el tipo de plan entre--> ")
    Plan_Utilizado = Plan_Utilizado.lower()
    Codigo_de_usuario = int(input("Ingrese su codigo de usuario--> "))
    nombre= input ("Ingrese su nombre--> ")
    Edad = int(input("Ingrese su edad --> "))
    
    if Plan_Utilizado  not in data:
        data[Plan_Utilizado]={}
    Utilizado["Nombre"] = nombre
    Utilizado["Edad"] = Edad
    data[Plan_Utilizado][Codigo_de_usuario] = Utilizado
    
    
     
Subcriptores = { 'premium' : { 28282:{ "Nombre": " Alejandro", "edad": 29}},
                'normal' : { 1095:{ "Nombre": " Ricardo", "edad": 23}},
                'plus' : { 10955:{ "Nombre": " Ricardo", "edad": 23}}
                }
while True:
    
    op = input("opcion 1 op 2 ")
    
    if op == "1":
        Registro_de_Datos (Subcriptores)
    if op == "2": 
        print(" Salio del sistema")
        break 
    if op == "3":
        for valor, llave in Subcriptores.items():
            print( valor, llave)
            

    
    
    
    
    
    
    

    
    