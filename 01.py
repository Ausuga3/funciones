#crear un arreglo de 20 nombres de personas, visualizar los elementos de la lista cada uno en una fila distinta



def crearLista(n):
    nombres=[]
    for i in range(n):
        nombre= input(f"ingrese el nombre {i+1}: ").capitalize()
        nombres.append(nombre)
    return nombres
    
def listarEnFila(lista):
    print("Lista de nombres: ")
    for i in lista:
        
        print(f"{i}")



if __name__=='__main__':
    numeroDeNombres= 20 #int(input("Digita cuantos nombres deseas crear: "))
    nombres=crearLista(numeroDeNombres)
    listarEnFila(nombres)
         