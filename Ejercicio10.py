'''
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
'''

def decimal_a_binario(numero):
    '''
    Definición: Función encargada de convertir un número decimal a binario\n
    Parámetros de entrada:\n
    numero-->El número decimal que se convertirá a binario\n
    Valor retorno:\n
    binario-->Número convertido a binario
    '''

    numerador=numero
    residuo=0
    cociente=0
    resultado = []
    binario = ""

    #Realizando las divisiones sucesivas
    while cociente != 1:
        residuo=numerador%2
        cociente=numerador//2
        resultado.append(residuo)
        #El nuevo numerador va a ser el antiguo cociente
        numerador=cociente
    resultado.append(cociente)
    resultado.reverse()

    #Covierte el número en cadena de caracteres
    for numero in resultado:
        binario += str(numero)
  
    return binario

def binario_a_decimal(num_binario):
    '''
    Definición: Función encargada de convertir un número binario a decimal\n
    Parámetros de entrada:\n
    num_binario-->El número en binario que se convertirá en decimal\n
    Valor de retorno:\n
    decimal-->Número en decimal
    '''

    decimal=0
    lista_numeros = list(num_binario)
    lista_numeros.reverse()
    for i in range(len(lista_numeros)):
        decimal+=int(lista_numeros[i])*(2**i)

    return decimal  

print(decimal_a_binario(23))
print(binario_a_decimal("10110"))