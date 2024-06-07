def buscar(valor, lista):
    posicion = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            posicion = i
            return posicion
    return posicion

# print(buscar("Gaseosa", dulces))

dulces = ["Chocolatina", "Nucita", "Frunas", "Gomitas"]
frutas = ["Manzana", "Pera", "Melon"]

#Agregar elemento al final
dulces.append("Gaseosa")
print(dulces)

#Agregar elementos de un iterable a la lista
dulces.extend(frutas)
print(dulces)

#Agregar en una posición específica
dulces.insert(3, "Quipitos")
print(dulces)

#Reemplazar un valor
dulces[4] = "Tomate"
print(dulces) 

#Eliminar por valor
dulces.append("Frunas")
print(dulces)
dulces.remove("Frunas")
print(dulces)

#Eliminar en un indice
print(dulces.pop(6))
print(dulces)
print(dulces.pop())
print(dulces)

#Eliminar todos los elementos
# dulces.clear()
# print(dulces)

#Impresión lista con formato personalizado
# for i in range(len(dulces)):
#     if i == len(dulces)-1:
#         print(i, dulces[i])
#     else:
#         print(i, dulces[i], " - ", end="")

#Contar cuantas veces está un elemento
dulces.append("Arequipe")
dulces.append("Arequipe")
print(dulces)
print(dulces.count("Arequipe"))

#Ordenar de forma ascendente
dulces.sort()
print(dulces)

#Invertir valores
dulces.reverse()
print(dulces)

#Saber si un elemento está en la lista
print("Arequipe" in dulces)
print("abc" in dulces)

#Saber si dos listas son la misma
lista_1 = [1,2,3]
lista_2 = lista_1
lista_3 = [1,2,3]

print(lista_1 is lista_2)
print(lista_1 is lista_3)

#Saber si almenos un elemento es verdadero
print("************************")
lista_4 = [""]
print(any(lista_4))
