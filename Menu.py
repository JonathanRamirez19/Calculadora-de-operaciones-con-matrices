from fractions import Fraction
import numpy as np
import sys

def imprimir_matriz(matriz):
    m, n = matriz.shape
    for i in range(m):
        for j in range(n):
            elemento = str(matriz[i, j])
            if '/' in elemento:
                numerador, denominador = elemento.split('/')
                print(f"{numerador.rjust(3)}/{denominador.ljust(3)}", end=' ')
            else:
                print(f"{elemento}".rjust(7), end=' ')
        print("\n")

def ingresar_matriz(m):
    matriz = np.empty((m, m), dtype=object)
    print("Introduce los elementos de la matriz (como fracciones, ej. '1/2', o números enteros):")
    for i in range(m):
        for j in range(m):
            entrada = input(f"Elemento [{i+1}, {j+1}]: ")
            matriz[i, j] = Fraction(entrada)
    return matriz

def calcular_determinante(matriz):
    matriz_float = np.array([[float(elemento) for elemento in fila] for fila in matriz])
    return np.linalg.det(matriz_float)

def imprimir_determinante(determinante):
    determinante_fraccion = Fraction(determinante).limit_denominator()
    print(f"El determinante de la matriz es: {determinante_fraccion}")

def calcular_adjunta(matriz):
    adjunta = np.linalg.inv(matriz) * np.linalg.det(matriz)
    adjunta_fraccion = np.vectorize(lambda x: Fraction(x).limit_denominator())(adjunta)
    return adjunta_fraccion

def calcular_determinante_y_adjunta():
    print("Cálculo del Determinante y la Matriz Adjunta con Entradas en Fracciones")
    m = int(input("Introduce el tamaño de la matriz cuadrada A (número de filas/columnas): "))
    matriz = ingresar_matriz(m)
    
    determinante = calcular_determinante(matriz)
    imprimir_determinante(determinante)

    matriz_np = np.array([[float(elemento) for elemento in fila] for fila in matriz], dtype=float)
    adjunta = calcular_adjunta(matriz_np)
    adjunta_fraccion = np.vectorize(lambda x: Fraction(x).limit_denominator())(adjunta)
    print("La matriz adjunta (en fracciones) es:")
    imprimir_matriz(adjunta_fraccion)

def calcular_matriz_inversa():
    print("Cálculo de la Matriz Inversa con Entradas en Fracciones")
    m = int(input("Introduce el número de renglones/columnas: "))
    matriz = ingresar_matriz(m)

    try:
        matriz_float = np.array([[float(value) for value in row] for row in matriz])
        inv_matriz_float = np.linalg.inv(matriz_float)
        inv_matriz = np.empty((m, m), dtype=object)
        for i in range(m):
            for j in range(m):
                inv_matriz[i, j] = Fraction.from_float(inv_matriz_float[i, j]).limit_denominator()
        print("La matriz inversa es (en fracciones):")
        imprimir_matriz(inv_matriz)
    except np.linalg.LinAlgError:
        print("La matriz no es invertible.")

def realizar_descomposicion_lu():
    print("Descomposición LU, matrices cuadradas")
    m = int(input("Introduce el número de renglones: "))
    matriz = ingresar_matriz(m)
    u = np.copy(matriz).astype(np.float64)  # Se modifica para iniciar U como una copia de la matriz de entrada
    l = np.eye(m).astype(np.float64)  # L se inicia como la matriz identidad

    for k in range(m):
        for i in range(k+1, m):
            factor = u[i, k] / u[k, k]
            u[i, k:] = u[i, k:] - factor * u[k, k:]
            l[i, k] = factor

    print("Resultados de Matriz L")
    l_fraccion = np.vectorize(lambda x: Fraction(x).limit_denominator())(l)
    imprimir_matriz(l_fraccion)
    print("Resultados de Matriz U")
    u_fraccion = np.vectorize(lambda x: Fraction(x).limit_denominator())(u)
    imprimir_matriz(u_fraccion)

def calcular_inversa_adjunta():
    print("Cálculo de la Matriz Inversa Adjunta")
    m = int(input("Introduce el número de renglones/columnas de A: "))
    print("Ahora introduce la matriz Adjunta de A:")
    adjunta = ingresar_matriz(m)

    det_matriz = Fraction(input("Introduce el determinante de A que se usará: "))
    if det_matriz == 0:
        print("La matriz es singular (no invertible), ya que el determinante es 0.")
        return

    try:
        adjunta_float = np.array([[float(value) for value in row] for row in adjunta])
        inversa_adjunta = adjunta_float / float(det_matriz)  # Convertir el determinante a float para la operación
        inversa_adjunta_fraccion = np.vectorize(lambda x: Fraction(x).limit_denominator())(inversa_adjunta)
        print("La matriz inversa adjunta es (en fracciones):")
        imprimir_matriz(inversa_adjunta_fraccion)
    except Exception as e:
        print(f"Ocurrió un error al calcular la inversa adjunta: {e}")


#################################################################


def calcular_gauss_jordan():
    n = int(input('Ingresa el tamaño de la matriz cuadrada: '))
    a = np.zeros((n,n+1))
    x = np.zeros(n)
    print('Ingresa los datos de la matriz empezando por filas:')
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]
                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    for i in range(n):
        x[i] = a[i][n]/a[i][i]
    print('\nLa solucion es: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')

###################################################################

def main():
    while True:
        print("\nMenú de Operaciones con Matrices:")
        print("1. Descomposición LU")
        print("2. Matriz Inversa")
        print("3. Determinante de Matriz y la Matriz Adjunta")
        print("4. Matriz Inversa Adjunta")
        print("5. Métodos de Gauss y Gauss-Jordan para solución de sistemas")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            realizar_descomposicion_lu()
        elif opcion == '2':
            calcular_matriz_inversa()
        elif opcion == '3':
            calcular_determinante_y_adjunta()
        elif opcion == '4':
            calcular_inversa_adjunta()
        elif opcion == '5':
            calcular_gauss_jordan()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
