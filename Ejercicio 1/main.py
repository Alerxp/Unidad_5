from random import sample
from Hash import Hash

if __name__ == '__main__':
    h_prima = Hash(1000, True)
    h_noprima = Hash(1000)

    claves = sample(range(1000, 10000), 1000)  # 1000 claves aleatorias sin repetir
    for clave in claves:
        h_prima.insertar(clave)
        h_noprima.insertar(clave)

    print("*** Hash Prima ***")
    h_prima.mostrar10()  # muestro las 10 primeras para después buscar alguna de esas claves
    print("\n*** Hash No Prima ***")
    h_noprima.mostrar10()

    clave = int(input("\nIngrese la clave a buscar: "))

    print("\n*** Hash Prima ***")
    pos = h_prima.buscar(clave)
    long = h_prima.longitud(clave)
    print(f"Longitud de la secuencia de prueba lineal: {long}")
    print("{}".format(f"Posición: {pos}" if pos is not None else "No existe esa clave"))

    print("\n*** Hash No Prima ***")
    pos = h_noprima.buscar(clave)
    long = h_noprima.longitud(clave)
    print(f"Longitud de la secuencia de prueba lineal: {long}")
    print("{}".format(f"Posición: {pos}" if pos is not None else "No existe esa clave"))
