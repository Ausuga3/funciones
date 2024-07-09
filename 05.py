#se te ha asignado la tarea de desarrollar un programa que cree y muestre los elementos de una matriz bidimencional de dimensiones 4x5,es decir, 4 filas y 5 columnas.Cada elemento de la matriz debe ser un numero entero generado aleatoriamente entre 1 y 100, inclusivo. Una vez generada, la matriz debe ser mostrada en pantalla, elemnto por elemento, junto con sus indices correspondientes para facilitar su identificacion.

import random
mat=[]

def createMatriz(n):
    for i in range(n):
        fila=[]
        for j in range(n):
            numeroAleatorio= random.randint(1,100)
            fila.append(numeroAleatorio)
        mat.append(fila)
    return mat



    """for i in range(4):
        for j in range(5):
            print(f"indice [{i},{j}]={mat[i][j]}")
        print("")    
    


    print("matriz generada: ")
    for fila in mat:
        for elemento in fila:
            print(f"{elemento:3}",end=" ")
        print()      """  
def imprimirLista(lista):
    for i in mat:
        print(i)


if __name__=='__main__':
    matriz=createMatriz(5)
    imprimirLista(matriz)