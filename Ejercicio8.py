'''
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
'''

#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
def estadistica(numeros):
    '''
    Definición: Función encargada de recibir una muestra de números en una lista y devolver un diccionario con su media, varianza y desviación típica.\n
    Parámetros de entrada:\n
    números-->Lista de número a la cual se les calculara su media, varianza y desviación típica.\n
    Valores de retorno:\n
    dic-->Diccionario que contiene la media, varianza y desviación típica de la lista de números
    '''
    #Cálculando la media de los números    
    media=0
    sumatoria=0
    for numero in numeros:
        sumatoria += numero
    media = sumatoria/len(numeros)

    #Cálculando la varianza de los números
    varianza =0
    sumatoria2=0
    for numero in numeros:
        sumatoria2+=(numero-media)**2
    varianza = sumatoria2/len(numeros)

    #Cálculando la desviación típica
    desviación_tipíca=(sumatoria2/(len(numeros)-1))**0.5

    #formando el diccionario con los datos
    dic={
        'media':media,
        'varianzan':varianza,
        'desviación_típica':desviación_tipíca
    }

    #Valor de retorno
    return dic

print(estadistica([1, 2, 3, 4, 5]))
print(estadistica([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

