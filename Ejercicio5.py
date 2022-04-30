'''
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
'''

#Función encargada de calcular el área de un círculo
def area_circulo(radio):
    '''Función encargada de calcular el área de un círculo'''
    area = 3.14159265359*(radio**2)
    return area

#Función encargada de calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    '''Función encargada de calcular el volumen de un cilindro'''
    volumen = area_circulo(radio)*altura
    return volumen

print(volumen_cilindro(3,5))