# INSTALAR UN PAQUETE SI NO EXISTE
```python
import importlib

def install_package_if_not_exists(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        import subprocess
        subprocess.check_call(['pip', 'install', package_name])

# Uso del método
package_name = 'pandas'
install_package_if_not_exists(package_name)
```
| Configuración | PostgreSQL     | MySQL |
|---------------|-----------|------------------------------|
| Host          | localhost | localhost                    |
| Port          | 5555      | 3333                         |
| User          | admin     | admin                        |
| Password      | 12345678  | 12345678                     |
| Database      | test_poc  | test_poc                     |
| Schema        | public    | test_poc                     |

# Cliente DBeaver para probar as conexiones

# Iniciar postgres con docker
```
docker run --name jorgecardona-postgres --rm -e POSTGRES_DB=test_poc -e POSTGRES_PASSWORD=12345678 -e POSTGRES_USER=admin -d -p 5555:5432 postgres:13.11-bullseye
```

# Probar el acceso a la base de datos
<img src="Contenedores\Bases de datos\probar_conexion_postgresql.png">

# Detener Contenedor postgres
```
docker stop jorgecardona-postgres
```

# Iniciar mysql con docker
```
docker run --name jorgecardona-mysql --rm -e MYSQL_DATABASE=test_poc -e MYSQL_PASSWORD=12345678 -e MYSQL_USER=admin -e MYSQL_ROOT_PASSWORD=root -d -p 3333:3306 mysql:8.0.33
```
# Probar el acceso a la base de datos
<img src="Contenedores\Bases de datos\probar_conexion_mysql.png">

# Detener Contenedor mysql
```
docker stop jorgecardona-mysql
```