import random
mat=[]

def createMatriz(num,num2):
    for i in range(num):
        fila=[]
        for j in range(num2):
            numeroAleatorio= random.randint(1,100)
            fila.append(numeroAleatorio)
        mat.append(fila)
    return mat

def imprimirLista(lista):
    for i in mat:
        print(i)


if __name__=='__main__':
    matriz=createMatriz(4,5)
    imprimirLista(matriz)