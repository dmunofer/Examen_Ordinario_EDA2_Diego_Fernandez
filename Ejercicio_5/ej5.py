def mochila_01(precio, pesos, pesomaximo):
    n = len(precio)
    # Crear una tabla de tamaño (n + 1) x (W + 1)
    tabla = [[0 for i in range(pesomaximo + 1)] for j in range(n + 1)]
    # Llenar la tabla iterativamente
    for i in range(1, n + 1):
        for w in range(1, pesomaximo + 1):
            if pesos[i-1] <= w:
                tabla[i][w] = max(precio[i-1] + tabla[i-1][w-pesos[i-1]], tabla[i-1][w])
            else:
                tabla[i][w] = tabla[i-1][w]
    return tabla[n][pesomaximo]

# Ejemplo de uso
# precio = [103, 60, 70, 5, 15]
# pesos = [12, 23, 11, 15, 7]
# peso_maximo = 100
# print(mochila_01(precio, pesos, peso_maximo))