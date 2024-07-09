#hacer un programa que lea las calificaciones de un alumno en 10 asignaturas, las almacene en una lista y calcule su media

def agregarNotas(cantidad):
    notas=[]
    for i in range(cantidad):
        nota=float(input(f"Ingrese la nota de su asignatura #{i+1}: "))
        notas.append(nota)
    return notas

def calcularMedia(lista,cantidad):
    return sum(lista)/cantidad



def main():
    cantidadNotas=10
    notas=agregarNotas(cantidadNotas)
    print(f"el promedio de las notas es {calcularMedia(notas,cantidadNotas)}")


if __name__=='__main__':
    main()