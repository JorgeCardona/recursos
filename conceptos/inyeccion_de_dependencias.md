# ✅ Abstracción

La abstracción en programación es cuando defines y  decides qué cosas puede hacer algo y qué cosas tiene, pero no te preocupas por los detalles de cómo lo hace. Solo usas lo que necesitas saber. Osea que métodos y propiedades debe tener algo, antes de crearlo.

Por ejemplo, imagina que tienes una clase "Robot":

El robot puede "caminar" y "hablar" (esos son sus métodos).

El robot tiene "color" y "tamaño" (esos son sus atributos).

No te importa saber cómo el robot camina o cómo funciona su voz, solo sabes que puedes usar esos botones para hacer que camine y hable. La abstracción es como usar el robot sin tener que entender todos sus detalles internos.

Es como cuando usas un juguete, solo sabes qué hace, no cómo lo hace.

# ✅ Modificadores de acceso
 Imagina que tienes diferentes cosas en casa: algunas las compartes con todos, otras solo con tu familia, otras con tus iguales y otras no las compartes con nadie.  
 
| Nivel de acceso | ¿Quién puede usarlo?                          | ¿Se comparte?           | Ejemplo claro para todos                                                                     |
|-----------------|-----------------------------------------------|--------------------------|-----------------------------------------------------------------------------------------------|
| `private`       | Solo tú                                       | No                       | Tu **ropa interior**: solo tú la usas, nadie más puede ni debe usarla.                       |
| `protected`     | Tú y tus hermanos                             | Sí, con hermanos         | La **bicicleta familiar**: solo tú y tus hermanos pueden usarla, no tus amigos.              |
| `default`       | Todos los que viven en tu casa (familia)      | Sí, dentro de casa       | El **control de la tele**: todos en casa pueden usarlo, pero nadie de afuera.                |
| `public`        | Todos (familia, amigos, vecinos)              | Sí, con cualquiera       | La **pelota del jardín**: todos pueden jugar con ella, incluso los visitantes.               |


---

### **1. `public`** – Se puede usar desde cualquier parte  
- **Cómo se hace:** sin guiones bajos  
- **Ejemplo:**
  ```python
  class Persona:
      nombre = "Juan"  # público
  ```

---

### **2. `protected`** – Se usa dentro de la clase y de sus subclases  
- **Cómo se indica:** con un **guion bajo delante**: `_nombre`  
- **Python no lo bloquea**, pero **es una forma de decir "no lo uses desde fuera"**
- **Ejemplo:**
  ```python
  class Persona:
      _edad = 10  # protegido (recomendación, no forzado)
  ```

---

### **3. `private`** – Solo dentro de la misma clase  
- **Cómo se indica:** con **dos guiones bajos delante**: `__nombre`  
- Python **lo renombra internamente** para que sea difícil acceder desde fuera.
- **Ejemplo:**
  ```python
  class Persona:
      __documento = "12345"  # privado
  ```

---

### ¿Y `default`?
En Python **no existe un nivel "por defecto" como en Java**, porque todo lo que no empieza con guión bajo se considera `public`.

```java
public class Persona {
    public String nombre;       // público
    protected int edad;         // protegido
    String ciudad;              // default (sin modificador)
    private String documento;   // privado
}
```

---
## En resumen:

### ¿Por qué importa esto en programación?
Porque igual que en tu casa decides quién puede usar tus cosas, en programación decides quién puede ver o usar partes del código. Esto ayuda a que todo funcione bien y nadie use lo que no debe.

| Nivel de acceso | Java (ejemplo)                     | Python (equivalente)      | Notas                                                                 |
|-----------------|------------------------------------|----------------------------|-----------------------------------------------------------------------|
| `public`        | `public String nombre;`            | `nombre = "Juan"`          | Visible desde cualquier parte.                                       |
| `protected`     | `protected int edad;`              | `_edad = 10`               | Visible dentro de la clase y subclases. En Python es solo convención.|
| `default`       | `String ciudad;` *(sin modificador)* | ❌ No existe              | En Java, visible solo en el mismo paquete. Python no tiene paquetes igual. |
| `private`       | `private String documento;`        | `__documento = "1234"`     | Solo accesible dentro de la clase. En Python se “manglea” el nombre. |

---

# ✅ Inyección de Dependencias

La inyección de dependencias es un patrón de diseño que permite que una clase principal no cree por sí misma los objetos que necesita, sino que los reciba desde afuera (ya construidos), por medio de diferentes mecanismos.  

Esto favorece la **separación de responsabilidades** en clases especializadas, y permite que la clase principal se enfoque en coordinar el flujo lógico de un proceso, usando esas piezas ya preparadas.

Una clase utiliza inyección de dependencias cuando recibe, como parámetros, instancias de otras clases a través de su **constructor**, **métodos setter**, o **métodos normales**, en lugar de crearlas por sí misma.

---

## 🔹 Estos objetos (llamados dependencias) se pueden inyectar de tres formas:
### 🔸 Como parámetros del constructor

Se inyecta el objeto al momento de crear la clase. Es obligatorio y se guarda internamente.

```python
class Asistente:
    def pasar_bisturi(self):
        print("Bisturí pasado.")

class Cirujano:
    def __init__(self, asistente: Asistente):
        self.asistente = asistente

    def operar(self):
        self.asistente.pasar_bisturi()
        print("Cirugía realizada.")

# Uso
asistente = Asistente()
cirujano = Cirujano(asistente)
cirujano.operar()
```

---

### 🔸 Como parámetros de un método setter

Se inyecta después de crear el objeto, usando un método `set_...`. Se guarda para usarse varias veces.

```python
class Asistente:
    def pasar_bisturi(self):
        print("Bisturí pasado.")

class Cirujano:
    def set_asistente(self, asistente: Asistente):
        self.asistente = asistente

    def operar(self):
        self.asistente.pasar_bisturi()
        print("Cirugía realizada.")

# Uso
asistente = Asistente()
cirujano = Cirujano()
cirujano.set_asistente(asistente)
cirujano.operar()
```

---

### 🔸 Como parámetros de un método cualquiera

Se pasa el objeto como parámetro al momento de usarlo. No se guarda; se usa puntualmente.

```python
class Asistente:
    def pasar_bisturi(self):
        print("Bisturí pasado.")

class Cirujano:
    def operar(self, asistente: Asistente):
        asistente.pasar_bisturi()
        print("Cirugía realizada.")

# Uso
asistente = Asistente()
cirujano = Cirujano()
cirujano.operar(asistente)
```

---

## 📋 Tabla Resumen

| Tipo de Inyección | ¿Cuándo se da la dependencia?    | ¿Se guarda? | ¿Cuándo usarla?                             |
|-------------------|----------------------------------|-------------|---------------------------------------------|
| Constructor       | Al crear el objeto               | Sí          | Si la dependencia es esencial desde el inicio |
| Setter (propiedad)| Después de crear el objeto       | Sí          | Si la necesitas varias veces, pero no al inicio |
| En Método         | Al llamar al método específico   | No          | Si la usás solo una vez y no la necesitás guardar |

---

## 🧁 Explicación Detallada con el Ejemplo del Pastel

### ❌ Sin Inyección de Dependencias

Una persona tendría que encargarse de **todo**:

- Fabricar el horno
- Sembrar y moler el trigo para la harina
- Criar gallinas para obtener huevos
- Alimentar vacas para la leche
- Cultivar caña para el azúcar
- Generar electricidad
- Conseguir agua
- Crear utensilios
- Cosechar frutas adicionales
- Transportar ingredientes

🔁 Resultado: Un proceso **extremadamente complejo y costoso** para solo hacer un pastel.

---

### ✅ Con Inyección de Dependencias

Recibe los ingredientes y utensilios **ya listos**.  
La persona consigue los ingredientes y utencilios que necesita, solo mezcla, hornea y coordina.  
En términos técnicos:  
> La clase principal **recibe sus dependencias ya construidas** a través de constructor, método setter o contenedor de inyecciones.

---

## 🧩 ¿Qué se logra con la inyección de dependencias?

### 1. **Desacoplamiento**
**Definición**: La clase principal (`Pastel`) no crea directamente sus dependencias. Se le inyectan desde fuera, lo que reduce su dependencia del código de bajo nivel.

```python
class IngredientesLiquidos:
    def __init__(self):
        self.leche = "200ml"
        self.huevos = "2 huevos"

class IngredientesSolidos:
    def __init__(self):
        self.harina = "300g"
        self.azucar = "100g"

class UtensiliosBasicos:
    def __init__(self):
        self.batidor = "batidor manual"

class UtensiliosAvanzados:
    def __init__(self):
        self.horno = "horno eléctrico"

class Pastel:
    def __init__(self, ingredientes_liquidos, ingredientes_solidos, utensilios_basicos, utensilios_avanzados):
        self.liquidos = ingredientes_liquidos
        self.solidos = ingredientes_solidos
        self.basicos = utensilios_basicos
        self.avanzados = utensilios_avanzados

    def batir(self):
        print(f"Usando {self.basicos.batidor} para mezclar {self.solidos.harina} con {self.liquidos.huevos}")
```

---

### 2. **Modularidad**
**Definición**: Cada clase representa un módulo independiente. Puedes cambiar una sin afectar las otras.

```python
# Si cambias solo el horno:
class HornoGas:
    def __str__(self):
        return "horno a gas"

class UtensiliosAvanzados:
    def __init__(self, horno):
        self.horno = horno

# Nada más cambia, el resto del sistema sigue igual.
pastel = Pastel(IngredientesLiquidos(), IngredientesSolidos(), UtensiliosBasicos(), UtensiliosAvanzados(HornoGas()))
```

---

### 3. **Flexibilidad**
**Definición**: Puedes reemplazar fácilmente cualquier dependencia por otra (otro batidor, otro horno).

```python
class BatidoraElectrica:
    def __str__(self):
        return "batidora eléctrica"

class UtensiliosBasicos:
    def __init__(self, batidor):
        self.batidor = batidor

# Cambiar el batidor sin tocar la clase Pastel
pastel = Pastel(IngredientesLiquidos(), IngredientesSolidos(), UtensiliosBasicos(BatidoraElectrica()), UtensiliosAvanzados())
```

---

### 4. **Reutilización**
**Definición**: Las clases como `IngredientesLiquidos` o `UtensiliosBasicos` pueden usarse en otras recetas.

```python
# Reutilizando en otro pastel
ingredientes_liquidos = IngredientesLiquidos()
ingredientes_solidos = IngredientesSolidos()

pastel_chocolate = Pastel(ingredientes_liquidos, ingredientes_solidos, UtensiliosBasicos(), UtensiliosAvanzados())
pastel_vainilla = Pastel(ingredientes_liquidos, ingredientes_solidos, UtensiliosBasicos(), UtensiliosAvanzados())
```

---

### 5. **Pruebas**
**Definición**: Puedes simular o inyectar versiones falsas de dependencias para pruebas unitarias.

```python
class HornoSimulado:
    def __str__(self):
        return "horno simulado para pruebas"

utensilios_avanzados = UtensiliosAvanzados()
utensilios_avanzados.horno = HornoSimulado()

# Se inyecta horno simulado sin modificar la lógica de Pastel
pastel = Pastel(IngredientesLiquidos(), IngredientesSolidos(), UtensiliosBasicos(), utensilios_avanzados)
```

---

### 6. **Mantenimiento sencillo**
**Definición**: Al estar desacoplado, si cambias una parte (como una nueva receta), no rompes el resto.

```python
class IngredientesSolidosNuevaReceta:
    def __init__(self):
        self.harina = "250g"
        self.azucar = "80g"

# Solo cambias los ingredientes, el resto del sistema no se toca
pastel = Pastel(IngredientesLiquidos(), IngredientesSolidosNuevaReceta(), UtensiliosBasicos(), UtensiliosAvanzados())
```

---

### 7. **Adaptabilidad**
**Definición**: Puedes introducir nuevas tecnologías (como hornos inteligentes) sin afectar el resto del sistema.

```python
class HornoInteligente:
    def __str__(self):
        return "horno inteligente conectado a WiFi"

utensilios_avanzados = UtensiliosAvanzados()
utensilios_avanzados.horno = HornoInteligente()

pastel = Pastel(IngredientesLiquidos(), IngredientesSolidos(), UtensiliosBasicos(), utensilios_avanzados)
```

---

### 8. **Escalabilidad**
**Definición**: Puedes agregar más ingredientes o herramientas fácilmente conforme crece el sistema.

```python
class IngredientesExtras:
    def __init__(self):
        self.chispas_chocolate = "50g"

class IngredientesSolidosExtendidos(IngredientesSolidos):
    def __init__(self):
        super().__init__()
        self.extras = IngredientesExtras()

# Nueva clase extendida con ingredientes extra
pastel = Pastel(IngredientesLiquidos(), IngredientesSolidosExtendidos(), UtensiliosBasicos(), UtensiliosAvanzados())
```

---

### 9. **Reducción de la complejidad**
**Definición**: La clase `Pastel` se mantiene limpia, sin preocuparse por cómo se crean las dependencias.

```python
# No hay lógica de creación dentro de Pastel
# Todo viene listo desde fuera

pastel = Pastel(IngredientesLiquidos(), IngredientesSolidos(), UtensiliosBasicos(), UtensiliosAvanzados())
```

---

### 10. **Coherencia**
**Definición**: El sistema sigue una estructura clara. Las dependencias están bien organizadas y visibles.

```python
# Estructura clara con nombres explícitos
pastel = Pastel(
    ingredientes_liquidos = IngredientesLiquidos(),
    ingredientes_solidos = IngredientesSolidos(),
    utensilios_basicos = UtensiliosBasicos(),
    utensilios_avanzados = UtensiliosAvanzados()
)
```


## 🧾 Conclusión

La inyección de dependencias ayuda a simplificar el proceso de desarrollo al evitar que las clases tengan que crear todo lo que necesitan por sí mismas. Esto permite que las clases solo se encarguen de lo que deben hacer, mientras que las dependencias (ya preparadas) se inyectan desde fuera, promoviendo un diseño más limpio, flexible y mantenible.

La inyección de dependencias **simplifica el desarrollo** al evitar que las clases tengan que construir por sí mismas lo que necesitan.  
Esto promueve un diseño:

- ✅ Limpio  
- ✅ Flexible  
- ✅ Mantenible  
- ✅ Probable y modular  

---
