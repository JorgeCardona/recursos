# ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS DEL PROYECTO VERSION 1
```
⭐ matematica_basica [project_directory]
┗ 🦄 src
    ┗ ⚽ __init__.py
    ┗ ♻️ elementales
       ┗ 💿 __init__.py
       ┗ 📀 funciones_basicas.py
    ┗ ⚜️ compuestos
       ┗ 💿 __init__.py
       ┗ 📀 funciones_avanzadas.py
┗ 🚀 test
  ┗ ⚽ __init__.py
  ┗ ⛔ elementales
     ┗ ⚽ __init__.py
     ┗ ✔️ test_funciones_basicas.py 
  ┗ 🎯 compuestos
     ┗ ⚽ __init__.py
     ┗ ✔️ test_funciones_avanzadas.py 
┗ 🔑 setup.py
┗ 🎁 README.md
┗ 🛒 requirements.txt
```

# ACCESO DIRECTO AL CODIGO DE CADA ARCHIVO DEL PROYECTO
⭐ matematica_basica [project_directory]
    ┗ 🦄 src [package]
    ┗ ⚽ [\__init__.py](#archivo-init)
    ┗ ♻️ elementales
        ┗ 💿 [\__init__.py](#codigo-init-elementales)
        ┗ 📀 [funciones_basicas.py](#codigo-funciones-basicas)
    ┗ ⚜️ compuestos
        ┗ 💿 [\__init__.py](#codigo-init-compuestos)
        ┗ 📀 [funciones_avanzadas.py](#codigo-funciones-avanzadas)
    ┗ 🚀 test
        ┗ ⚽ [\__init__.py](#archivo-init)
        ┗ ⛔ elementales
            ┗ ⚽ [\__init__.py](#archivo-init)
            ┗ ✔️ [test_funciones_basicas.py](#codigo-test-funciones-basicas) 
        ┗ 🎯 compuestos
            ┗ ⚽ [\__init__.py](#archivo-init)
            ┗ ✔️ [test_funciones_avanzadas.py](#codigo-test-funciones-avanzadas) 
    ┗ 🔑 [setup.py](#codigo-setup-v1)
    ┗ 🎁 [README.md](#documentacion-mark-down)
    ┗ 🛒 [requirements.txt](#paquetes-requirements)

# crear la carpeta **Publicar Paquetes PyPI**

# Abrir la carpeta con un IDE de desarrollo, por ejemplo **Visual Studio Code**
<img src="..\imagenes\01_abrir_con_code.png">

# Abrir una Terminal
<img src="..\imagenes\02_abrir_terminal.png">

# Crea el entorno virtual
## `virtualenv venv`

<img src="..\imagenes\03_crear_el_entorno_virtual.png">

# Activa el entorno virtual
# LINUX
## `source venv/bin/activate`

# WINDOWS
## `venv/Scripts/activate`

<img src="..\imagenes\04_activar_entorno_virtual.png">

# Actualiza PIP
## `python.exe -m pip install --upgrade pip`
<img src="..\imagenes\05_actualizar_pip.png">

# Crear La estructura del Proyecto y adicionar el codigo del `README.md`, segun sea el caso

<img src="..\imagenes\06_crear_estructura_del_proyecto.png">

# Instalar los requerimientos del proyecto
<img src="..\imagenes\07_instalar_requirements.png">

# Ejecuta las pruebas unitarias para validar que todo este OK
## `pytest -v`

# Reporte de pruebas unitarias
<img src="..\imagenes\08_ejecutar_pruebas_unitarias.png">


# Instala las dependencias para generar los binarios y publicar a PyPI test, y PyPI
# pero si uso la instalacion de requirements.txt, este paso no es necesario
## `python -m pip install --upgrade setuptools wheel twine`
<img src="..\imagenes\09_instalar_paquetes_necesarios.png">

# Genera el archivo Binario instalable de la version 1
# Se crea la carpeta build, dist y MiPaquetePublicable.egg-info
## `python setup.py sdist bdist_wheel`
<img src="..\imagenes\10_generar_el_binario.png">


# Instalar el paquete en local machine/environment para probar el paquete
## `pip install -e .`
<img src="..\imagenes\11_instalar_el_paquete_en_local.png">

# validar si el paquete esta instalado
## `pip list`

# validar la informacion de la version instalada
## `pip show MiPaquetePublicable`
<img src="..\imagenes\12_validar_el_paquete_instalado.png">

# Verificar funcionalidad del paquete
# [Módulo de Cálculos Matemáticos Elementales](#uso-funciones-basicas)
# [Módulo de Cálculos Matemáticos Compuestos Avanzados](#uso-funciones-avanzadas)

# desinstalar el paquete instalado
## `pip uninstall MiPaquetePublicable -y`

# Publicar el paquete en Test PyPI
## Crear una cuenta en https://test.pypi.org/account/register/
## `twine upload --repository testpypi dist/* --verbose`
<img src="..\imagenes\13_publicar_en_test_pypi.png">

# Instalar el paquete desde Test PyPI
<img src="..\imagenes\14_validar_e_instalar_paquete_desde_test_pypi.png">
## `pip install -i https://test.pypi.org/simple/ MiPaquetePublicable==0.0.1`
<img src="..\imagenes\15_instalar_paquete_desde_test_pypi.png">

# validar si el paquete esta instalado
## `pip list `

# validar la informacion de la version instalada
## `pip show MiPaquetePublicable`
<img src="..\imagenes\12_validar_el_paquete_instalado.png">

# Verificar funcionalidad del paquete, en el `README.md` con el codigo en la seccion de cada Módulo
# [Módulo de Cálculos Matemáticos Elementales](#uso-funciones-basicas)
# [Módulo de Cálculos Matemáticos Compuestos Avanzados](#uso-funciones-avanzadas)
<img src="..\imagenes\21_validacion_de_codigo.png">

# LA IMPORTANCIA DEL NOMBRE DEL PAQUETE
### *AUNQUE VEMOS QUE PAQUETE SE LLAMA <span style="color: blue;"> MiPaquetePublicable </span> PARA USAR LAS FUNCIONES ES NECESARIO LLAMAR SU DIRECTORIO <span style="color: red;"> elementales </span> Y MODULO <span style="color: green;"> funciones_basicas </span>, DIRECTORIO <span style="color: orange;"> compuestos </span> Y MODULO <span style="color: pink;"> funciones_avanzadas </span> Y NUNCA SE USO DIRECTAMENTE EL NOMBRE DEL MODULO PUBLICADO* 

# crear una nueva version 0.0.2 del paquete modificando el archivo setup
# [setup.py](#codigo-setup-v2)

# Genera el Segundo archivo Binario instalable
## `python setup.py sdist bdist_wheel`

<img src="..\imagenes\16_generar_segundo_binario.png">

# Publicar el paquete en Test PyPI
## `twine upload --repository testpypi dist/* --verbose`

# En Ocasiones Falla la publicacion, porque hay una version en dist, que ya fue publicada
# elminar la carpeta dist, build y todo lo que no creamos en el proyecto, incluyendo los archivos de pytest, volver a reintentar publicar, ahora todo OK!. 
## `twine upload --repository testpypi dist/* --verbose`
<img src="..\imagenes\17_publicar_en_test_pypi.png">

# desinstalar el paquete instalado
## `pip uninstall MiPaquetePublicable -y`
<img src="..\imagenes\18_desinstalar_paquete.png">

# Publicar el paquete en PyPI oficial
## Crear una cuenta en https://pypi.org/account/register/
## `python -m twine upload dist/* --verbose`
<img src="..\imagenes\19_publicar_en_pypi_oficial.png">

# Instalar el paquete desde PyPI
<img src="..\imagenes\20_validar_e_instalar_paquete_desde_pypi_oficial.png">

## `pip install MiPaquetePublicable`

# validar la informacion de la version instalada
## `pip show MiPaqueteDePrueba`
<img src="..\imagenes\12_validar_el_paquete_instalado.png">

# Verificar funcionalidad del paquete, en el `README.md` con el codigo en la seccion de cada Módulo
# [Módulo de Cálculos Matemáticos Elementales](#uso-funciones-basicas-2)
# [Módulo de Cálculos Matemáticos Compuestos Avanzados](#uso-funciones-avanzadas-2)
<img src="..\imagenes\21_validacion_de_codigo.png">

# desinstalar el paquete instalado
## `pip uninstall MiPaquetePublicable -y`
<img src="..\imagenes\18_desinstalar_paquete.png">


# CODIGO DE LA APLICACION
---
# Paquetes Requirements
```python
# en el la archivo requirements.txt
# copiar estos paquetes a instalar
setuptools==68.0.0
wheel==0.41.0
twine==4.0.2
pytest==7.4.0
jupyterlab==4.0.3
```

# Archivo init
```python
# crear este archivo en la carpeta solicitada SIN NINGUN CONTENIDO 
__init__.py
```

# Codigo setup v1
```python
# en el directorio raiz del proyecto matematica_basica
# crear el archivo set_up.py y adicionar el siguiente codigo

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="MiPaquetePublicable",
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

# Codigo Setup v2
```python
# en el directorio raiz del proyecto matematica_basica
# reemplazar el codigo del set_up.py y adicionar el siguiente codigo

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="MiPaquetePublicable",
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

# Codigo init Elementales
```python
# en el directorio version_1\matematica_basica\src\elementales\__init__.py
# crear el archivo __init__.py y adicionar el siguiente codigo
from .funciones_basicas import CalculosMatematicosElementales
```

# Codigo Funciones Basicas
```python
# en el directorio version_1\matematica_basica\src\elementales\funciones_basicas.py
# crear el archivo funciones_basicas.py y adicionar el siguiente codigo
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


# Codigo init Compuestos
```python
# en el directorio version_1\matematica_basica\src\compuestos\__init__.py
# crear el archivo __init__.py y adicionar el siguiente codigo
from .funciones_avanzadas import CalculosMatematicosCompuestos
```

# Codigo Funciones Avanzadas
```python
# en el directorio version_1\matematica_basica\src\compuestos\funciones_avanzadas.py
# crear el archivo funciones_avanzadas.py y adicionar el siguiente codigo
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
    def factorial(n: int) -> int:
        """
        Calcula el factorial de un número entero no negativo (n).

        Parameters:
            n (int): El número entero del cual se calculará el factorial.

        Returns:
            int: El resultado del factorial de n.

        Raises:
            ValueError: Si n es un número entero negativo.

        Examples:
            >>> factorial(5)
            El factorial de 5 es 120
            120

            >>> factorial(0)
            El factorial de 0 es 1
            1

            >>> factorial(10)
            El factorial de 10 es 3628800
            3628800

        Note:
            El factorial de un número entero no negativo n (representado por n!) es el producto
            de todos los enteros positivos desde 1 hasta n. Por convención, se define que el
            factorial de 0 es 1.
        """
        if n < 0:
            raise ValueError("El factorial solo está definido para números enteros no negativos.")
        
        print(f'El factorial de {n} es {math.factorial(n)}')
        return math.factorial(n)

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

# Codigo Test Funciones Basicas
```python
# en el directorio version_1\matematica_basica\test\elementales\test_funciones_basicas.py
# crear el archivo test_funciones_basicas.py y adicionar el siguiente codigo

import unittest
from src.elementales.funciones_basicas import CalculosMatematicosElementales

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

# Codigo Test Funciones Avanzadas
```python
# en el directorio version_1\matematica_basica\test\compuestos\test_funciones_avanzadas.py
# crear el archivo test_funciones_avanzadas.py y adicionar el siguiente codigo

import unittest
import pytest
from src.compuestos.funciones_avanzadas import CalculosMatematicosCompuestos

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

# Documentacion Mark Down
```python
# en el directorio raiz del proyecto matematica_basica
# crear el archivo README.md y adicionar el siguiente codigo
```

# Módulo de Cálculos Matemáticos Elementales

Este módulo proporciona diversas funciones para realizar cálculos matemáticos elementales, incluyendo operaciones de suma, resta, multiplicación, división decimal y división entera.

# Uso Funciones Basicas

Para utilizar este módulo, simplemente importa la clase `CalculosMatematicosElementales` desde `elementales` y llama a los métodos estáticos correspondientes.

```python
from elementales.funciones_basicas import CalculosMatematicosElementales

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

# Uso Funciones Avanzadas

Para utilizar este módulo, simplemente importa la clase `CalculosMatematicosCompuestos` desde `compuestos` y llama a los métodos estáticos correspondientes.

```python
from compuestos.funciones_avanzadas import CalculosMatematicosCompuestos

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
```












