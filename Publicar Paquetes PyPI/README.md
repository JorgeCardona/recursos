# crear la carpeta **Publicar Paquetes PyPI**

# Abrir la carpeta con un IDE de desarrollo, por ejemplo **Visual Studio Code**
<img src="imagenes\01_abrir_con_code.png">

# Abrir una Terminal
<img src="imagenes\02_abrir_terminal.png">

# Crea el entorno virtual
```bash
virtualenv venv
```
<img src="imagenes\03_crear_el_entorno_virtual.png">

# Activa el entorno virtual
```bash
# LINUX
source venv/bin/activate

# WINDOWS
venv/Scripts/activate
```
<img src="imagenes\04_activar_entorno_virtual.png">

# Actualiza PIP, e Instala Jupyterlab y pytest
```bash
(venv) jorge@cardona:~$ python.exe -m pip install --upgrade pip
(venv) jorge@cardona:~$ pip install jupyterlab pytest
```
<img src="imagenes\05_instalar_jupyter_lab_pytest.png">

# Inicia jupyter Lab
```bash
jupyter lab
```
<img src="imagenes\06_iniciar_jupyter_lab.png">


# Crea un directorio del proyecto a publicar
```yaml
matematica_basica
```

# Se ubica en el directorio creado matematica_basica
```
cd matematica_basica
```
# Crea el modulo basicos y su __init__.py
```yaml
matematica_basica\src\elementales\basicos.py
matematica_basica\src\elementales\__init__.py
```
# Copia el codigo de este modulo
```python
class CalculosMatematicosElementales:

    @staticmethod
    def suma(x: float, y: float) -> float:
        """
        Realiza la suma de dos números.

        Parameters:
            x (float): Primer número a sumar.
            y (float): Segundo número a sumar.

        Returns:
            float: Resultado de la suma.
        """
        print(f'El resultado de la SUMA {x} + {y} es {x + y}')
        return x + y

    @staticmethod
    def resta(x: float, y: float) -> float:
        """
        Realiza la resta de dos números.

        Parameters:
            x (float): Número al que se le restará el otro número.
            y (float): Número que se restará al primer número.

        Returns:
            float: Resultado de la resta.
        """
        print(f'El resultado de la RESTA  {x} - {y} es {x - y}')
        return x - y
    
    @staticmethod
    def multiplicacion(x: float, y: float) -> float:
        """
        Realiza la multiplicación de dos números.

        Parameters:
            x (float): Primer número a multiplicar.
            y (float): Segundo número a multiplicar.

        Returns:
            float: Resultado de la multiplicación.
        """
        print(f'El resultado de la MULTIPLICACION  {x} * {y} es {x * y}')
        return x * y
    
    @staticmethod
    def division_decimal(x: float, y: float) -> float:
        """
        Realiza la división decimal de dos números.

        Parameters:
            x (float): Número que se dividirá.
            y (float): Número por el cual se dividirá.

        Returns:
            float: Resultado de la división decimal.
        """
        print(f'El resultado de la DIVISIÓN DECIMAL {x} / {y} es {x / y}')
        return x / y
    
    @staticmethod
    def division_entera(x: int, y: int) -> int:
        """
        Realiza la división entera de dos números.

        Parameters:
            x (int): Número que se dividirá.
            y (int): Número por el cual se dividirá.

        Returns:
            int: Resultado de la división entera.
        """
        print(f'El resultado de la DIVISIÓN ENTERA {x} // {y} es {x // y}')
        return x // y
```

# Codigo del __init__.py
```python
from .basicos import CalculosMatematicosElementales
```

# Crea el modulo avanzados y su __init__.py
```yaml
matematica_basica\src\compuestos\avanzados.py
matematica_basica\src\compuestos\__init__.py
```
# Copia el codigo de este modulo
```python
import math

class CalculosMatematicosCompuestos:
    @staticmethod
    def potencia(x: float, y: float) -> float:
        """
        Calcula la potencia de x elevado a y y muestra el resultado.

        Parameters:
            x (float): El número base.
            y (float): El exponente.

        Returns:
            float: El resultado de la potencia.
        """
        print(f'El resultado de la POTENCIA {x} elevado a {y} es {x ** y}')
        return x ** y

    @staticmethod
    def raiz_cuadrada(x: float, y: float) -> float:
        """
        Calcula la raiz cuadrada del valor absoluto de (x + y) y muestra el resultado.

        Parameters:
            x (float): Primer número.
            y (float): Segundo número.

        Returns:
            float: El resultado de la raiz cuadrada.
        """
        print(f'El resultado de la raiz cuadrada del valor absoluto de {x} + {y} es {math.sqrt(abs(x + y))}')
        return math.sqrt(abs(x + y))

    @staticmethod
    def logaritmo(x: float, y: float) -> float:
        """
        Calcula el logaritmo del valor absoluto de x en base y y muestra el resultado.

        Parameters:
            x (float): El número del cual se calculará el logaritmo.
            y (float): La base del logaritmo.

        Returns:
            float: El resultado del logaritmo.
        """
        print(f'El logaritmo del valor absoluto de {x} en base {y} es {math.log(abs(x), abs(y))}')
        return math.log(abs(x), abs(y))

    @staticmethod
    def piso(x: float, y: float) -> int:
        """
        Calcula el piso de la división de x entre y y muestra el resultado.

        Parameters:
            x (float): Numerador.
            y (float): Denominador.

        Returns:
            int: El resultado del piso.
        """
        print(f'El piso de {x} dividido {y} es {math.floor(x / y)}')
        return math.floor(x / y)

    @staticmethod
    def techo(x: float, y: float) -> int:
        """
        Calcula el techo de la división de x entre y y muestra el resultado.

        Parameters:
            x (float): Numerador.
            y (float): Denominador.

        Returns:
            int: El resultado del techo.
        """
        print(f'El techo de {x} dividido {y} es {math.ceil(x / y)}')
        return math.ceil(x / y)

    @staticmethod
    def factorial(x: float, y: float) -> int:
        """
        Calcula la suma del factorial de x más la suma del factorial de y y muestra el resultado.

        Parameters:
            x (float): Primer número.
            y (float): Segundo número.

        Returns:
            int: El resultado de la suma del factorial.
        """
        print(f'La suma del factorial de {x} más la suma del factorial de {y} es {math.factorial(abs(x)) + math.factorial(abs(y))}')
        return math.factorial(abs(x)) + math.factorial(abs(y))

    @staticmethod
    def imaginarios(x: complex, y: complex) -> complex:
        """
        Calcula la multiplicación de dos números imaginarios x e y y muestra el resultado.

        Parameters:
            x (complex): Primer número imaginario.
            y (complex): Segundo número imaginario.

        Returns:
            complex: El resultado de la multiplicación de los números imaginarios.
        """
        print(f'La multiplicación del número imaginario {x} con el número imaginario {y} es {x * y}')
        return x * y
```

# Codigo del __init__.py
```python
from .avanzados import CalculosMatematicosCompuestos
```

# Crea las pruebas unitarias
```
matematica_basica\test\test_calculos_matematicos_avanzados.py
matematica_basica\test\test_calculos_matematicos_basicos.py
```

# codigo test_calculos_matematicos_basicos.py
```python
import unittest
from src.elementales.basicos import CalculosMatematicosElementales

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
```

# codigo test_calculos_matematicos_avanzados.py
```python
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
```

# Ejecuta las pruebas unitarias con pytest
```yaml
pytest -v
```

# reporte de pruebas unitarias
```yaml
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.9.2rc1, pytest-7.4.0, pluggy-1.2.0 -- jorge@cardona\Publicar Paquetes PyPI\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: jorge@cardona\Publicar Paquetes PyPI\matematica_basica
plugins: anyio-3.7.1
collected 12 items

test/test_calculos_matematicos_avanzados.py::TestCalculosMatematicosCompuestos::test_potencia PASSED                                                                                                     [  8%] 
test/test_calculos_matematicos_avanzados.py::TestCalculosMatematicosCompuestos::test_raiz_cuadrada PASSED                                                                                                [ 16%] 
test/test_calculos_matematicos_avanzados.py::TestCalculosMatematicosCompuestos::test_logaritmo PASSED                                                                                                    [ 25%] 
test/test_calculos_matematicos_avanzados.py::TestCalculosMatematicosCompuestos::test_piso PASSED                                                                                                         [ 33%] 
test/test_calculos_matematicos_avanzados.py::TestCalculosMatematicosCompuestos::test_techo PASSED                                                                                                        [ 41%] 
test/test_calculos_matematicos_avanzados.py::TestCalculosMatematicosCompuestos::test_factorial PASSED                                                                                                    [ 50%] 
test/test_calculos_matematicos_avanzados.py::TestCalculosMatematicosCompuestos::test_imaginarios PASSED                                                                                                  [ 58%] 
test/test_calculos_matematicos_basicos.py::TestCalculosMatematicosElementales::test_division_decimal PASSED                                                                                              [ 66%] 
test/test_calculos_matematicos_basicos.py::TestCalculosMatematicosElementales::test_division_entera PASSED                                                                                               [ 75%] 
test/test_calculos_matematicos_basicos.py::TestCalculosMatematicosElementales::test_multiplicacion PASSED                                                                                                [ 83%]
test/test_calculos_matematicos_basicos.py::TestCalculosMatematicosElementales::test_resta PASSED                                                                                                         [ 91%] 
test/test_calculos_matematicos_basicos.py::TestCalculosMatematicosElementales::test_suma PASSED                                                                                                          [100%] 

============================================================================================= 12 passed in 0.11s ==============================================================================================
```

# Generar la documentacion del README.md
### INICIO README.md
--------------------------------------------------------------------------
# Módulo de Cálculos Matemáticos Elementales

Este módulo proporciona diversas funciones para realizar cálculos matemáticos elementales, incluyendo operaciones de suma, resta, multiplicación, división decimal y división entera.

## Uso

Para utilizar este módulo, simplemente importa la clase `CalculosMatematicosElementales` desde `elementales` y llama a los métodos estáticos correspondientes.

```python
# from elementales.basicos import CalculosMatematicosElementales
from elementales import CalculosMatematicosElementales

# Ejemplo de uso del método de suma
resultado_suma = CalculosMatematicosElementales.suma(2, 3)
print(resultado_suma)  # Salida: El resultado de la SUMA 2.0 + 3.0 es 5.0

# Ejemplo de uso del método de resta
resultado_resta = CalculosMatematicosElementales.resta(10, 5)
print(resultado_resta)  # Salida: El resultado de la RESTA 10.0 - 5.0 es 5.0

# Ejemplo de uso del método de multiplicación
resultado_multiplicacion = CalculosMatematicosElementales.multiplicacion(4, 3)
print(resultado_multiplicacion)  # Salida: El resultado de la MULTIPLICACION 4.0 * 3.0 es 12.0

# Ejemplo de uso del método de división decimal
resultado_division_decimal = CalculosMatematicosElementales.division_decimal(10, 3)
print(resultado_division_decimal)  # Salida: El resultado de la DIVISIÓN DECIMAL 10.0 / 3.0 es 3.3333333333333335

# Ejemplo de uso del método de división entera
resultado_division_entera = CalculosMatematicosElementales.division_entera(10, 3)
print(resultado_division_entera)  # Salida: El resultado de la DIVISIÓN ENTERA 10 // 3 es 3
```

## Métodos disponibles

A continuación se enumeran los métodos disponibles en la clase `CalculosMatematicosElementales`:

- `suma(x: float, y: float) -> float`: Realiza la suma de dos números.

- `resta(x: float, y: float) -> float`: Realiza la resta de dos números.

- `multiplicacion(x: float, y: float) -> float`: Realiza la multiplicación de dos números.

- `division_decimal(x: float, y: float) -> float`: Realiza la división decimal de dos números.

- `division_entera(x: int, y: int) -> int`: Realiza la división entera de dos números.

## Notas

- Recuerda que para utilizar este módulo, asegúrate de tener instalado Python.

- Los métodos `suma`, `resta`, `multiplicacion`, `division_decimal` y `division_entera` funcionan con números reales.

- La división decimal puede producir resultados con una precisión limitada en números decimales repetitivos.

# Módulo de Cálculos Matemáticos Compuestos Avanzados

Este módulo proporciona diversas funciones para realizar cálculos matemáticos compuestos avanzados, incluyendo operaciones de potencia, raíz cuadrada, logaritmo, piso, techo, factorial y multiplicación de números imaginarios.

## Uso

Para utilizar este módulo, simplemente importa la clase `CalculosMatematicosCompuestos` desde `compuestos` y llama a los métodos estáticos correspondientes.

```python
# from compuestos.avanzados import CalculosMatematicosCompuestos
from compuestos import CalculosMatematicosCompuestos

# Ejemplo de uso del método de potencia
resultado_potencia = CalculosMatematicosCompuestos.potencia(2, 3)
print(resultado_potencia)  # Salida: El resultado de la POTENCIA 2 elevado a 3 es 8

# Ejemplo de uso del método de raiz cuadrada
resultado_raiz = CalculosMatematicosCompuestos.raiz_cuadrada(9, 16)
print(resultado_raiz)  # Salida: El resultado de la raiz cuadrada del valor absoluto de 9 + 16 es 5.0

# Ejemplo de uso del método de logaritmo
resultado_logaritmo = CalculosMatematicosCompuestos.logaritmo(10, 100)
print(resultado_logaritmo)  # Salida: El logaritmo del valor absoluto de 10 en base 100 es 0.5

# Ejemplo de uso del método de piso
resultado_piso = CalculosMatematicosCompuestos.piso(7, 2)
print(resultado_piso)  # Salida: El piso de 7 dividido 2 es 3

# Ejemplo de uso del método de techo
resultado_techo = CalculosMatematicosCompuestos.techo(7, 2)
print(resultado_techo)  # Salida: El techo de 7 dividido 2 es 4

# Ejemplo de uso del método de factorial
resultado_factorial = CalculosMatematicosCompuestos.factorial(5)
print(resultado_factorial)  # Salida: El factorial de 5 es 120

# Ejemplo de uso del método de multiplicación de números imaginarios
resultado_imaginarios = CalculosMatematicosCompuestos.imaginarios(2j, 3j)
print(resultado_imaginarios)  # Salida: La multiplicación del número imaginario 2j con el número imaginario 3j es -6
```

## Métodos disponibles

A continuación se enumeran los métodos disponibles en la clase `CalculosMatematicosCompuestos`:

- `potencia(x: float, y: float) -> float`: Calcula la potencia de x elevado a y.

- `raiz_cuadrada(x: float, y: float) -> float`: Calcula la raiz cuadrada del valor absoluto de (x + y).

- `logaritmo(x: float, y: float) -> float`: Calcula el logaritmo del valor absoluto de x en base y.

- `piso(x: float, y: float) -> int`: Calcula el piso de la división de x entre y.

- `techo(x: float, y: float) -> int`: Calcula el techo de la división de x entre y.

- `factorial(n: int) -> int`: Calcula el factorial de un número entero no negativo n.

- `imaginarios(x: complex, y: complex) -> complex`: Calcula la multiplicación de dos números imaginarios x e y.

## Notas

- Recuerda que para utilizar este módulo, asegúrate de tener instalado Python y el módulo math.

- Si el método `factorial` es llamado con un número entero negativo, se lanzará una excepción `ValueError`.

- Los métodos `piso` y `techo` devuelven resultados como enteros.

- El método `imaginarios` opera con números imaginarios utilizando el operador `*`.

- Si deseas más detalles sobre cada método, consulta la documentación en el código fuente.

- Para ejecutar las pruebas unitarias, puedes utilizar el framework `unittest` o `pytest` y verificar que cada método funcione correctamente.
--------------------------------------------------------------------------
### FIN README.md

# Genera el archivo setup.py con la configuracion e informacion del paquete, para generar los binarios
```yaml
# python3 setup.py sdist bdist_wheel
import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="MiPaqueteDePrueba",
    version="0.0.1",
    author="Jorge Cardona",
    description="Descripción del paquete",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JorgeCardona/recursos/Publicar Paquetes PyPI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

# Instala las dependencias para generar los binarios y publicar a PyPI test, y PyPI
```bash
python -m pip install --upgrade setuptools wheel twine
```

# Genera el archivo Binario instalable
```python
python setup.py sdist bdist_wheel
```

# Instalar el paquete en local machine/environment para probar el paquete
```
pip install -e .
```

# validar si el paquete esta instalado
```
pip list
```
# validar la informacion de la version instalada
```
pip show MiPaqueteDePrueba
```

# Verificar funcionalidad del paquete, en el README.md con el codigo en la seccion de uso en
- Módulo de Cálculos Matemáticos Elementales
- Módulo de Cálculos Matemáticos Compuestos Avanzados

# desinstalar el paquete instalado
```
pip uninstall MiPaqueteDePrueba -y
```

# Publicar el paquete en Test PyPI
## Crear una cuenta en https://test.pypi.org/account/register/
```bash
twine upload --repository testpypi dist/* --verbose
```

# Instalar el paquete desde Test PyPI
```
pip install ...
```

# validar si el paquete esta instalado
```
pip list
```
# validar la informacion de la version instalada
```
pip show MiPaqueteDePrueba
```

# Verificar funcionalidad del paquete, en el README.md con el codigo en la seccion de uso en
- Módulo de Cálculos Matemáticos Elementales
- Módulo de Cálculos Matemáticos Compuestos Avanzados

# crear una nueva version 0.0.2 del paquete modificando el setup.py
```yaml
# python3 setup.py sdist bdist_wheel
import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="MiPaqueteDePrueba",
    version="0.0.2",
    author="Jorge Cardona",
    description="Descripción del paquete",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JorgeCardona/recursos/Publicar Paquetes PyPI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

# Genera el archivo Binario instalable
```python
python setup.py sdist bdist_wheel
```

# Publicar el paquete en Test PyPI
```bash
twine upload --repository testpypi dist/* --verbose
```
# Falla la publicacion, porque hay una version en dist, que ya fue publicada
# elminar la carpeta dist, build y todo lo que no creamos en el proyecto, incluyendo los archivos de pytest, volver a reintentar publicar, ahora todo OK!. 
```bash
twine upload --repository testpypi dist/* --verbose
```

# desinstalar el paquete instalado
```
pip uninstall MiPaqueteDePrueba -y
```

# Publicar el paquete en PyPI oficial
## Crear una cuenta en https://pypi.org/account/register/
```bash
python -m twine upload dist/* --verbose
```

# Instalar el paquete desde PyPI
```
pip install ...
```

# validar si el paquete esta instalado
```
pip list
```
# validar la informacion de la version instalada
```
pip show MiPaqueteDePrueba
```

# Verificar funcionalidad del paquete, en el README.md con el codigo en la seccion de uso en
- Módulo de Cálculos Matemáticos Elementales
- Módulo de Cálculos Matemáticos Compuestos Avanzados

# desinstalar el paquete instalado
```
pip uninstall MiPaqueteDePrueba -y
```