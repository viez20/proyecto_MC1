import math

print("¡Bienvenido al Programa! \n\nSeleccione 2 números que conformen un rango comprendido entre 0 a 99,999.")
a = int(input("Ingrése el primer número (0 a 99,999): "))
b = int(input("Ingrése el segundo número (0 a 99,999): "))

print("\nAhora ingrese la cantidad de números que desee utilizar en el rango que se analizará.")
n = int(input("Ingrése cuántos números desea analizar (1 a 100,000): "))

#Se utilizó el "Método Lineal Congruencial" para la generación de números aleatorios uniformes. Específicamente se utilizaron módulos, multiplicadores e incrementos para la realización de este paso.
def aleatorios(valor_inicial, a, c, m):
    return (a * valor_inicial + c) % m

#Los 4 "Enteros Mágicos" para la generación de números aleatorios según el libro "The Art of Computer Programming Vol. 2 - Seminumerical Algorithms 3rd. Edition (Donald E. Knuth)":
# m = módulo; a = multiplicador; c = incremento; valor_inicial = Vo

def aleatorios_unicos(valor_inicial, inicial, final, n):
    if n > (final - inicial +1): #Verificador de cantidad de números a tomar en cuenta en el rango.
        raise ValueError("La cantidad de números que desea está fuera del rango permitido.") #Lo siguiente expresa que la función recibe un argumento correcto pero con valor inválido y ayuda a evitar valores inválidos.

    a = 1103515245 #Constante entera definida por el estándar "POSIX C" para la generación de números aleatorios.
    c = 12345 #Constante entera definida por el estándar "POSIX C" para la generación de números aleatorios. A parte estará de base en caso sólo se tome uno del rango.
    m = 2**31 #Garantiza que cubra un rango amplio de valores eficiente cuando se trabaja con números enteros de 32 bits.
    numeros = set() #Números aleatorios únicos.
    
    while len(numeros) < n: #Obtiene la cantidad de elementos y verifica si el número de elementos es menor que "n (cantidad de números para analizar)"
        valor_inicial = aleatorios(valor_inicial, a, c, m)
        numero_aleatorio = inicial + (valor_inicial % (final - inicial + 1)) #Número aleatorio dentro del rango.
        numeros.add(numero_aleatorio) #'numero_aleatorio' determina que 'numeros' contenga números que no se repitan dentro del rango.

    return sorted(list(numeros)) #Convierte 'numeros' en una lista, la ordena de forma ascendente y "devuelve" la lista ordenada.

inicial = min(a, b)
final = max (a, b)

if not (0 <= a <= 99999 and 0 <= b <= 99999): #Verificación para 'a' y 'b' si se encuentran en el rango.
    raise ValueError("Use rangos entre 0 y 99,999")

if n > (final - inicial + 1): #Comprobación de números aleatorios únicos.
    raise ValueError("No se exceda de la cantidad de números que son permitidos en el rango")

valor_inicial = int(math.sqrt(a * b)) #Generación de Aleatorios
numeros_aleatorios = aleatorios_unicos(valor_inicial, inicial, final, n)

print("\nLos números aleatorios basados en la cantidad de números que se analizarán son los siguientes:\n")
print(numeros_aleatorios)