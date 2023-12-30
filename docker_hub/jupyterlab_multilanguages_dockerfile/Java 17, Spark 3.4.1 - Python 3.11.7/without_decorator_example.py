from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def check_menu():
    return "Please bring me the menu"

def select_dish():
    return "I know what I want to eat"

def place_order():
    return "I would like chicken curry, please"

def enjoy_food():
    return "Excellent dinner"

dag = DAG('restaurant_routine_example_without_decorator', description='DAG for restaurant without decorator',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

step_one = PythonOperator(task_id='check_menu', python_callable=check_menu, dag=dag)
step_two = PythonOperator(task_id='select_dish', python_callable=select_dish, dag=dag)
step_three = PythonOperator(task_id='place_order', python_callable=place_order, dag=dag)
step_four = PythonOperator(task_id='enjoy_food', python_callable=enjoy_food, dag=dag)

step_one >> step_two >> step_three >> step_four
