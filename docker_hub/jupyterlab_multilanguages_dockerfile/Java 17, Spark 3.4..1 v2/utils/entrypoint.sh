#!/bin/bash
set -e

# Inicializa la base de datos de Airflow
airflow db init

# Crea el usuario administrador
airflow users create --role Admin --username admin --email admin@jorgecardona.com --firstname jorge --lastname cardona --password 12345678

# Inicia el servicio web de Airflow en segundo plano
airflow webserver -p 8081 &

# Inicia el programador de Airflow en segundo plano
airflow scheduler &

# Inicia JupyterLab
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --LabApp.token=''
