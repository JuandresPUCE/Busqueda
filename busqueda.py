def busquedaLineal(lista, elemento):
    print ("La lista es: ",lista )
    for indice in range(len(lista)):
        if lista[indice] == elemento:
             print("El indice es: ")
             return indice
        
    return print("elemento no existe")


def busquedaBinaria(lista,elemento):
    print ("La lista es: ",lista )
    # Nota el Arreglo debe estar ordenado
    lista.sort()
    print ("La lista está ordenada : ",lista )
    tamanoLista = len(lista)
    inicio = 0
    fin=tamanoLista-1

    while inicio<=fin:
        medio=(inicio+fin)//2
        if lista[medio] == elemento:
            print("El indice es: ")
            return  medio
        elif lista[medio] < elemento:
            inicio=medio+1
        elif lista[medio] > elemento:
            fin = medio-1

    return -1
# https://uniwebsidad.com/libros/algoritmos-python/capitulo-8/busqueda-binaria
# https://www.aluracursos.com/blog/busqueda-binaria-implementar-python


#Prueba de escritorio

lista = [11, 4, 5, 7, 8, 10, 778]
print(busquedaLineal(lista, 11))
print(busquedaBinaria(lista, 11))
