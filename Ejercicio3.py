'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

def factorial(numero):
    '''Función encargada de encontrar el factorial de
    numero'''
    #Recorriendo la secuencia descendiente
    factorial = 1
    for i in range(numero, 1, -1):
        factorial *= i
    return factorial

print(factorial(4))
print(factorial(20))