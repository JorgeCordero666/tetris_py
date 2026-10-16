# Crear una matriz de 5 filas y 5 columnas y modificar una celda concreta.
matriz = [
    [0,0,0,0,0], # 0
    [0,0,0,0,0], # 1
    [0,0,0,0,0], # 2
    [0,0,0,0,0], # 3
    [0,0,0,0,0], # 4
]  # 0 1 2 3 4

# Modificacion del primer valor 0,0
matriz[0][0] = 26
# Modificacion del valor de la fila 0, columna 1
matriz[0][1] = 33
# Modificacion del valor de la fila 0, columna 2
matriz[0][2] = 50

# Modificacion del primer valor de la fila 3, columna 0
matriz[3][0] = 12
# Modificacion del valor de la fila 3, columna 2
matriz[3][1] = 43
# Modificacion del valor de la fila 3, columna 3
matriz[3][3] = 98

# Imprimir en formato de matriz
# Por Posiciones
filas = range(len(matriz)) 
for fil in filas:
    print(matriz[fil],'\n')
# Directamente
for fila in matriz:
    print(*fila)
# Por elemento
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print() # Salto de linea