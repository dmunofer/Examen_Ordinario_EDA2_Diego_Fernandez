from Ejercicio_5 import ej5
def test_mochila_01():
    precio = [103, 60, 70, 5, 15]
    pesos = [12, 23, 11, 15, 7]
    peso_maximo = 100
    result = ej5.mochila_01(precio, pesos, peso_maximo)
    assert result == 253