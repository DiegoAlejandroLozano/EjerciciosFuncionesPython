'''
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
'''

#Función encargada de recibir una lista de número y devolver otra lista con sus cuadrados
def cuadrados_lista(numeros):
    '''
    Definición: Esta función se encarga de recibir una lista de números y de devolver otra lista
    con sus cuadrados.

    Parámetros de entrada:\n
    numeros-->Lista a la cual se le calculara el cuadra a cada uno de su valores

    Valor de retorno:\n
    cuadrados-->Lista que contiene el cuadrado de cada uno de los números de la 
    lista de entrada
    '''
    cuadrados = []

    for numero in numeros:
        cuadrados.append(numero**2)
    return cuadrados

print(cuadrados_lista([1, 2, 3, 4, 5]))
print(cuadrados_lista([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))