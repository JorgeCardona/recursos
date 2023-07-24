import math
import unittest
import pytest
from src.compuestos.avanzados import CalculosMatematicosCompuestos

class TestCalculosMatematicosCompuestos:

    # Prueba para el método potencia
    def test_potencia(self):
        """
        Prueba el método potencia de la clase CalculosMatematicosCompuestos.

        Comprueba si el método devuelve el resultado correcto al elevar un número (x) a una potencia (y).

        Casos de prueba:
        - Se verifica si 2 elevado a 3 es igual a 8.
        - Se verifica si 5 elevado a 0 es igual a 1.
        - Se verifica si 2 elevado a -3 es igual a 0.125.
        """
        assert CalculosMatematicosCompuestos.potencia(2, 3) == 8
        assert CalculosMatematicosCompuestos.potencia(5, 0) == 1
        assert CalculosMatematicosCompuestos.potencia(2, -3) == 0.125

    # Prueba para el método raiz_cuadrada
    def test_raiz_cuadrada(self):
        """
        Prueba el método raiz_cuadrada de la clase CalculosMatematicosCompuestos.

        Comprueba si el método devuelve la raíz cuadrada del valor absoluto de (x + y).

        Casos de prueba:
        - Se verifica si la raíz cuadrada de 9 + 16 es igual a 5.0.
        - Se verifica si la raíz cuadrada de 0 + 25 es igual a 5.0.
        - Se verifica si la raíz cuadrada de -16 + 25 es igual a 3.0.
        """
        assert CalculosMatematicosCompuestos.raiz_cuadrada(9, 16) == 5.0
        assert CalculosMatematicosCompuestos.raiz_cuadrada(0, 25) == 5.0
        assert CalculosMatematicosCompuestos.raiz_cuadrada(-16, 25) == 3.0

    # Prueba para el método logaritmo
    def test_logaritmo(self):
        """
        Prueba el método logaritmo de la clase CalculosMatematicosCompuestos.

        Comprueba si el método devuelve el logaritmo del valor absoluto de x en base y.

        Casos de prueba:
        - Se verifica si el logaritmo de 10 en base 100 es igual a 0.5.
        - Se verifica si el logaritmo de 1 en base 10 es igual a 0.0.
        - Se verifica si el logaritmo de 100 en base 10 es igual a 2.0.
        """
        assert CalculosMatematicosCompuestos.logaritmo(10, 100) == 0.5
        assert CalculosMatematicosCompuestos.logaritmo(1, 10) == 0.0
        assert CalculosMatematicosCompuestos.logaritmo(100, 10) == 2.0

    # Prueba para el método piso
    def test_piso(self):
        """
        Prueba el método piso de la clase CalculosMatematicosCompuestos.

        Comprueba si el método devuelve el piso de la división de x entre y.

        Casos de prueba:
        - Se verifica si el piso de 7 dividido 2 es igual a 3.
        - Se verifica si el piso de -10 dividido 3 es igual a -4.
        - Se verifica si el piso de 1 dividido 5 es igual a 0.
        """
        assert CalculosMatematicosCompuestos.piso(7, 2) == 3
        assert CalculosMatematicosCompuestos.piso(-10, 3) == -4
        assert CalculosMatematicosCompuestos.piso(1, 5) == 0

    # Prueba para el método techo
    def test_techo(self):
        """
        Prueba el método techo de la clase CalculosMatematicosCompuestos.

        Comprueba si el método devuelve el techo de la división de x entre y.

        Casos de prueba:
        - Se verifica si el techo de 7 dividido 2 es igual a 4.
        - Se verifica si el techo de -10 dividido 3 es igual a -3.
        - Se verifica si el techo de 1 dividido 5 es igual a 1.
        """
        assert CalculosMatematicosCompuestos.techo(7, 2) == 4
        assert CalculosMatematicosCompuestos.techo(-10, 3) == -3
        assert CalculosMatematicosCompuestos.techo(1, 5) == 1

    # Prueba para el método factorial

    def test_factorial(self):
        """
        Prueba el método factorial de la clase tu_modulo.

        Comprueba varios casos de prueba con diferentes valores.

        Casos de prueba:
        - Se verifica si el factorial de 5 es igual a 120.
        - Se verifica si el factorial de 0 es igual a 1.
        - Se verifica si el factorial de 10 es igual a 3628800.
        - Se verifica si el método lanza un ValueError al calcular el factorial de -5.
        """
        # Caso de prueba: factorial(5)
        assert CalculosMatematicosCompuestos.factorial(5) == 120

        # Caso de prueba: factorial(0)
        assert CalculosMatematicosCompuestos.factorial(0) == 1

        # Caso de prueba: factorial(10)
        assert CalculosMatematicosCompuestos.factorial(10) == 3628800

        # Caso de prueba: factorial(-5)
        with pytest.raises(ValueError):
            CalculosMatematicosCompuestos.factorial(-5)
  
    # Prueba para el método imaginarios
    def test_imaginarios(self):
        """
        Prueba el método imaginarios de la clase CalculosMatematicosCompuestos.

        Comprueba si el método devuelve la multiplicación de dos números imaginarios x e y.

        Casos de prueba:
        - Se verifica si la multiplicación de 2j con 3j es igual a -6j.
        - Se verifica si la multiplicación de 0j con 1j es igual a 0j.
        - Se verifica si la multiplicación de -1j con 2j es igual a -2j.
        """
        assert CalculosMatematicosCompuestos.imaginarios(2j, 3j) == -6
        assert CalculosMatematicosCompuestos.imaginarios(0j, 1j) == 0j
        assert CalculosMatematicosCompuestos.imaginarios(-1j, 2j) == 2

if __name__ == '__main__':
    unittest.main()