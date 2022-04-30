'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado 
con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
'''

def frecuencia(frase):
    '''
    Definición: Función encargada de determinar la frecuencia de cada palabra dentro 
    de una frase\n
    Parámetros:\n
    frase-->Este parametro representa la frese que se va a analizar\n
    Valor retorno:\n
    diccionario-->Contiene todas las palabras y su frecuencia
    '''

    palabras = frase.split()
    diccionario = {}

    #Recorriendo la lista de palabras
    for palabra in palabras:
        diccionario[palabra] = palabras.count(palabra)

    #Devolviendo el diccionario
    return diccionario

def palabra_mas_repetida(diccionario):
    '''
    Definición: Función encargada de determinar la palabra más repetida en la frase\n
    Parámetros:\n
    diccionario-->Diccionario con palabras y su frecuencia\n
    Valor retorno\n
    palabra_repetida-->Tupla con la palabra más repetida y su frecuencia
    '''
    
    lista_valores=diccionario.values() 
    maximo=max(lista_valores)
    elementos=diccionario.items()
    for elemento in elementos:
        if maximo == elemento[1]:
            return elemento 

texto = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"
print(frecuencia(texto))
print(palabra_mas_repetida(frecuencia(texto)))
