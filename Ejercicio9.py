'''
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
'''

def maximo_comun_divisor(num1, num2):
    '''
    Definición: Función encargada de calcular el máximo común divisor de dos números\n
    Parámetros:\n
    num1-->Es el primer número\n
    num2-->Es el segundo número\n
    Retorno:\n
    maximo_comun-->Máximo común divisor de los dos números\n
    '''

    #Rangos de números para encontrar los divisores exactos
    rango1 = range(1, num1+1)
    rango2 = range(1, num2+1)

    #Encontrando los números que dividen exactamente a num1
    divisores1 = []
    for numero in rango1:
        if num1%numero == 0:
            divisores1.append(numero)

    #Encontrando los números que dividen exactamente a num2
    divisores2 = []
    for numero in rango2:
        if num2%numero == 0:
            divisores2.append(numero)

    #Encontrando a los divisores comunes:
    divisores_comunes = []
    for i in divisores1:
        for j in divisores2:
            if i == j:
                divisores_comunes.append(i)

    #Encontrando el divisor mayor
    divisores_comunes.sort()
    maximo_comun = divisores_comunes[len(divisores_comunes)-1]

    return maximo_comun

def minimo_comun_multiplo(num1, num2):
    '''
    Definición: Función encargada de calcular el mínimo común múltiplo de dos números\n
    Parámetros:\n
    num1-->Es el primer número\n
    num2-->Es el segundo número\n
    Retorno:\n
    minino_comun-->Mínimo común multiplo de los dos números
    '''

    minimo_comun = (num1*num2)/maximo_comun_divisor(num1,num2)
    return int(minimo_comun)

print(maximo_comun_divisor(24,36))
print(minimo_comun_multiplo(24,36))