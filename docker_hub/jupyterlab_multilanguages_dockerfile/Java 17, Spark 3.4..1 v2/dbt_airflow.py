from airflow.decorators import dag, task
from airflow.operators.bash_operator import BashOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime
from time import sleep

@dag(schedule_interval='0 5 * * *', concurrency=10, max_active_runs=3, start_date=datetime(2021, 1, 1), catchup=False, tags=['DBT_START'])
def dbt_run_from_airflow():
    directory = '/notebooks/dbt_poc'
    
    def change_directory():
        command = f'cd {directory} && pwd'  # Example command, you can replace it with your specific command
        return command  # Returning the command

    def show_version():
        command = f'dbt -v'
        return command  # Returning the command

    def test_connection():
        command = f'cd {directory} && dbt debug'
        return command  # Returning the command

    def run_dbt():
        command = f'cd {directory} && dbt run'
        return command  # Returning the command

    def generate_documentation():
        command = f'cd {directory} && dbt docs generate'
        return command  # Returning the command

    def start_documentation_server():
        command = f'cd {directory} && dbt docs serve'
        return command  # Returning the command

    change_directory_task = BashOperator(
        task_id='change_directory_bash_task',
        bash_command=change_directory(),
    )

    show_version_task = BashOperator(
        task_id='show_version_bash_task',
        bash_command=show_version(),
    )

    test_connection_task = BashOperator(
        task_id='test_connection_bash_task',
        bash_command=test_connection(),
    )

    run_dbt_task = BashOperator(
        task_id='run_dbt_bash_task',
        bash_command=run_dbt(),
    )

    generate_documentation_task = BashOperator(
        task_id='generate_documentation_bash_task',
        bash_command=generate_documentation(),
    )

    start_documentation_server_task = BashOperator(
        task_id='start_documentation_server_bash_task',
        bash_command=start_documentation_server(),
    )

    change_directory_task >> show_version_task >> test_connection_task >> run_dbt_task >> generate_documentation_task >> start_documentation_server_task

dag_dbt_run = dbt_run_from_airflow()


@dag(schedule_interval='0 5 * * *', concurrency=10, max_active_runs=3, start_date=datetime(2021, 1, 1), catchup=False, tags=['DBT_STOP'])
def dbt_documentation_server_stop():

    def stop_documentation_server():
        sleep(5)  # stop server on these seconds
        command = f'pkill -f "dbt docs serve"'
        return command  # Returning the command	

    stop_documentation_server_task = BashOperator(
        task_id='stop_documentation_server_bash_task',
        bash_command=stop_documentation_server(),
    )

    stop_documentation_server_task

dag_stop_server = dbt_documentation_server_stop()
