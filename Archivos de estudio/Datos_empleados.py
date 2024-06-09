import json

Empleados = []

RUTA_ARCHIVO = "Registro_Empleados.json"

def guardar_datos_Empleados(Empleados):
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(Empleados, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos_Empleados():
    global RUTA_ARCHIVO
    Empleados = []
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            datos = json.load(file)
            if isinstance(datos, list):
                for Empleado in datos:
                    Empleados.append(Empleado)

        print("Datos cargados exitosamente!!")
        return Empleados
    except Exception:
        print("Error al cargar datos")
        return []