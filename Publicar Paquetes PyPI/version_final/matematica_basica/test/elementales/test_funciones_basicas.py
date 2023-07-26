import unittest
from src.FuncionesMatematicas.elementales.funciones_basicas import CalculosMatematicosElementales

class TestCalculosMatematicosElementales(unittest.TestCase):
    """
    Pruebas unitarias para la clase CalculosMatematicosElementales.

    La clase TestCalculosMatematicosElementales contiene una serie de pruebas
    unitarias para cada método de la clase CalculosMatematicosElementales. 
    Utiliza el módulo unittest para realizar las pruebas y verificar si los 
    métodos producen los resultados esperados en diferentes escenarios.
    """

    def test_suma(self):
        """
        Prueba la funcionalidad del método suma.

        Verifica si el resultado devuelto por el método suma coincide con el valor 
        esperado para diferentes casos de prueba.
        """
        self.assertEqual(CalculosMatematicosElementales.suma(3, 5), 8)
        self.assertEqual(CalculosMatematicosElementales.suma(0, 0), 0)
        self.assertEqual(CalculosMatematicosElementales.suma(-3, 5), 2)

    def test_resta(self):
        """
        Prueba la funcionalidad del método resta.

        Verifica si el resultado devuelto por el método resta coincide con el valor 
        esperado para diferentes casos de prueba.
        """
        self.assertEqual(CalculosMatematicosElementales.resta(8, 3), 5)
        self.assertEqual(CalculosMatematicosElementales.resta(0, 0), 0)
        self.assertEqual(CalculosMatematicosElementales.resta(-3, 5), -8)

    def test_multiplicacion(self):
        """
        Prueba la funcionalidad del método multiplicacion.

        Verifica si el resultado devuelto por el método multiplicacion coincide con el valor 
        esperado para diferentes casos de prueba.
        """
        self.assertEqual(CalculosMatematicosElementales.multiplicacion(3, 5), 15)
        self.assertEqual(CalculosMatematicosElementales.multiplicacion(0, 5), 0)
        self.assertEqual(CalculosMatematicosElementales.multiplicacion(-3, 5), -15)

    def test_division_decimal(self):
        """
        Prueba la funcionalidad del método division_decimal.

        Verifica si el resultado devuelto por el método division_decimal coincide con el valor 
        esperado para diferentes casos de prueba con números de punto flotante.
        """
        self.assertAlmostEqual(CalculosMatematicosElementales.division_decimal(10, 3), 3.3333333, places=4)
        self.assertAlmostEqual(CalculosMatematicosElementales.division_decimal(5, 2), 2.5, places=4)
        self.assertAlmostEqual(CalculosMatematicosElementales.division_decimal(7, 7), 1.0, places=4)

    def test_division_entera(self):
        """
        Prueba la funcionalidad del método division_entera.

        Verifica si el resultado devuelto por el método division_entera coincide con el valor 
        esperado para diferentes casos de prueba.
        """
        self.assertEqual(CalculosMatematicosElementales.division_entera(10, 3), 3)
        self.assertEqual(CalculosMatematicosElementales.division_entera(5, 2), 2)
        self.assertEqual(CalculosMatematicosElementales.division_entera(7, 7), 1)

if __name__ == '__main__':
    unittest.main()