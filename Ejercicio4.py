'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe 
recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si 
se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''

#Función  encargada de calcular el IVA
def iva(cantidad, porcentaje_iva=21):
    '''La función se encarga de calcular el IVA a un producto. Se devuelve el total de la factura.'''
    total_factura = ((porcentaje_iva/100)+1)*cantidad
    return total_factura

print(iva(1000, 10))
print(iva(1000))