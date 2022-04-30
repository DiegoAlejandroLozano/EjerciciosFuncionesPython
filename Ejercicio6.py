'''
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
'''

#Función encargada de cálcula la media de una lista de números
def media(lista_numeros):
    '''
    Definición: Función encargada de calcular la media de una lista de números

    parámetros de entrada:\n
    lista_numeros --> Lista de números a la cual se le calculara su media    
    
    valor de retorno:\n
    media --> Retorna la media de la lista de números
    '''
    suma = 0
    for numero in lista_numeros:
        suma += numero
    media = suma/len(lista_numeros)
    return media

print(media([1, 2, 3, 4, 5]))
print(media([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
