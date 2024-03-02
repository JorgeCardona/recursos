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
# Crear una imagen Docker de un Contenedor
```
docker commit ID_del_contenedor mi_aplicacion:version_1.0
docker commit 77a654ba0872 jorgecardona/datascience:v1
```

# Python Code
```python
import subprocess

# Parameter you want to pass to the shell script
parameter = "VERSION1"
parameter = "VERSION2"
parameter = "VERSION_ALTERNATIVA"

# Execute the shell script with the parameter
subprocess.run(["sh", "script.sh", parameter], check=True)
```

# Bash Code
```bash
#!/bin/bash

# Print the value of the parameter passed from Python
echo "The Original parameter value passed is: $1"

# Capture the parameter sent from Python and convert it to lowercase
notification_version=$(echo "$1" | tr '[:upper:]' '[:lower:]')

# Print the value of the parameter passed from Python
echo "The parameter passed on lower case version is: $notification_version"

# Initialize the variable message
message=""

# Assign value to the message variable based on the value of notification_version
if [ "$notification_version" = "version1" ]; then
    message="❌ The file 📜 \"$1\" 📜 was not found on Server. ❌"
elif [ "$notification_version" = "version2" ]; then
    message="❌ The file 📜 \"$1\" 📜 was not found on Server. ❌"
else
    message="❌ The files 📜 \"$1\" 📜 were not found on Server. ❌"
fi

# Print the value of message
echo "The message is: $message"

# Email notification content
subject="Subject: $ENV - ⚠️ Timeout reached ⚠️. Please check."
receiver_email="To: $MAIN_EMAIL"
receiver_email_copy="CC: $CC_EMAIL"
message_content="📢 ⏰ Timeout reached. $message. 🆘 Please review the processing steps 🆘 before rerunning the Airflow DAG 🔗‍💥 VALIDATION_PROCESS_SERVER 🛠️. ⏰ 🚑"

# Combine email content
final_message="$subject\n$receiver_email\n$receiver_email_copy\n\n$message_content"

# Print email content
echo "$final_message"

# Sending notification
echo "Sending email notification..."
echo "Timeout reached. Sending out email notification."
echo -e "$subject"
echo -e "$receiver_email"
echo -e "$receiver_email_copy"
echo -e "$message_content"
echo "Executing sendmail command..."

# Actual sendmail command
echo -e "Subject: $subject\n$receiver_email\n$receiver_email_copy\n\n$message_content" | sendmail $MAIN_EMAIL,$CC_EMAIL
```
