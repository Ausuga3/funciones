def listaNombres():
    return 'ana','maria','juan','aja','eylin'


def busqueda(lista,termino):
    listaNueva=[i for i in lista if termino in i]
    print(listaNueva) 
    

def main():
    listaOriginal=listaNombres()
    termino=input("que letra o cadena de letras deseas buscar en la lista: ")
    busqueda(listaOriginal,termino)

if __name__=='__main__':

    main()