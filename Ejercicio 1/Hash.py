import numpy as np

class Hash:
    def __init__(self, dimension, primo=False):
        # factor de carga 0.7
        self.__capacidad = round(self.__buscaPrimo(dimension) / 0.7) if primo else round(dimension / 0.7)
        self.__array = np.full(self.__capacidad, None)

    def __buscaPrimo(self, n):
        """
        Si n es un número primo lo devuelve, de lo contrario
        lo incrementa hasta que sea primo.

        Args:
            n (int): número entero

        Returns:
            n (int): número primo
        """
        from math import sqrt
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return self.__buscaPrimo(n+1)
        return n

    def __pruebaLineal(self, clave):
        pos = self.__funcionHash(clave)
        while self.__array[pos] is not None and self.__array[pos] != clave:
            pos = self.__funcionHash(pos + 1)
        return pos

    def __funcionHash(self, clave):
        return clave % self.__capacidad

    def insertar(self, clave):
        pos = self.__pruebaLineal(clave)
        self.__array[pos] = clave

    def buscar(self, clave):
        pos = self.__pruebaLineal(clave)
        if self.__array[pos] == clave:
            return pos
        else:
            return None

    def longitud(self, clave):
        pos = self.__funcionHash(clave)
        cont = 0
        while self.__array[pos] is not None and self.__array[pos] != clave:
            pos = self.__funcionHash(pos + 1)
            cont += 1
        return cont

    def borrar(self, clave):
        pos = self.buscar(clave)
        if pos is not None:
            self.__array[pos] = None
        else:
            print("No existe esa clave")

    def mostrar10(self):
        print(self.__array[:10])
