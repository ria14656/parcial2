# Definir la función que calcula la superficie de un rectángulo
def superficie_rectangulo(lado1, lado2):
  # Multiplicar los dos lados y retornar el resultado
  return lado1 * lado2

# Cargar los lados de dos rectángulos
lado1_rectangulo1 = 10
lado2_rectangulo1 = 5
lado1_rectangulo2 = 8
lado2_rectangulo2 = 6

# Llamar a la función para cada rectángulo y guardar los resultados
superficie_rectangulo1 = superficie_rectangulo(lado1_rectangulo1, lado2_rectangulo1)
superficie_rectangulo2 = superficie_rectangulo(lado1_rectangulo2, lado2_rectangulo2)

# Mostrar cual de los dos rectángulos tiene una superficie mayor
if superficie_rectangulo1 > superficie_rectangulo2:
  print("El rectángulo 1 tiene una superficie mayor que el rectángulo 2")
elif superficie_rectangulo1 < superficie_rectangulo2:
  print("El rectángulo 2 tiene una superficie mayor que el rectángulo 1")
else:
  print("Los dos rectángulos tienen la misma superficie")
