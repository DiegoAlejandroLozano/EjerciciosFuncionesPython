'''
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
'''

def saludo(nombre):
    '''Función encargada de realizar un saludo
    personalizado a través del parámetro nombre'''
    print("¡hola %s!" % str(nombre))

saludo("Diego")