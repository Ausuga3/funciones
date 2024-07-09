"""Escribe un programa en python que realice las siguientes acciones:
1-inicialice una lista vacia llamada notas para almacenar calificaciones de los estudiantes.
2-Solicite al usuario que ingrese 10 notas.Cada nota debe ser un numero decimal y se almacenara en la lista de notas.
3-soliite al usuario que ingrese una nota especifica que desea buscar en la lista de notas.
4-busque todas las posiciones en la lista donde se encuentre la nota especificada ppor el usuario y almacene estas posiciones en una lista de llamadas posiciones
5-verigique si la nota especificada se encontro en la lista.
6-so emcpmtraron posiciones, imprima las posiciones(basadas en 1, no en 0) donde se encuentra la nota
7. si la nota no se encontro en la lista, imprima un mensje indicandoque la nota no se encontro.
"""

def crearListaNotas(cantidad):
    notas=[]

    for i in range(cantidad):
        nota=float(input(f"Ingrese la nota #{i+1}: "))
        notas.append(nota)
    return notas

def busquedaEspecifica(nota,lista):
    posiciones=[]
    for i,n in enumerate(lista):
        if n == nota:
            posiciones.append(i+1)
    return posiciones

def main():
    numeroDeNotas=3
    notas = crearListaNotas(numeroDeNotas)

    notaABuscar= float(input("Ingrese la nota que deseas buscar: "))
    posiciones = busquedaEspecifica(notaABuscar,notas)

    if posiciones:
        print(f"la nota {notaABuscar} se encontro en la posicion {posiciones}")
    else:
        print("no se encontro la nota en la lista!!")


if __name__=='__main__':
    main()            



