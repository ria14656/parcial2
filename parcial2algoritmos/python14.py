def funcion():
    valor=[]
    for x in range(3):
        ingresar_valor=int(input('Ingrese el valor: '))
        valor.append(ingresar_valor)
    suma=0
    for x in range(3):
        suma=suma+valor[x]
    return suma/3

print(funcion())
