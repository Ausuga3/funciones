#crea una tupla con la informacion de un participante del torneo de ajedrez y luego imprime cada uno de los elementos dela tupla con una descripcion adecuada.

def crearParticipante():
    participante=["John Doe",30,"Canada",2400]
    return participante

def mostrarParticipante(participante):
    print(f"Nombre del participante: {participante[0]}")
    print(f"Edad del participante: {participante[1]}")
    print(f"Nacionalidad del participante: {participante[2]}")
    print(f"Calificacion elo: {participante[3]}")


if __name__=='__main__':
    participante=crearParticipante()
    mostrarParticipante(participante)    