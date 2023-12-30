from airflow.decorators import dag, task
from datetime import datetime

# https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html
# https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parsing-processes
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#worker-concurrency
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-runs-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#max-active-tasks-per-dag
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#parallelism
@dag(schedule_interval='0 5 * * *', concurrency=10,  max_active_runs=3, start_date=datetime(2021, 1, 1), catchup=False, tags=['Lunch'])
def restaurant_routine_example_with_decorator():
    
    @task()
    def check_menu():
        return "Please bring me the menu"

    @task()
    def select_dish():
        return "I know what I want to eat"

    @task()
    def place_order():
        return "I would like chicken curry, please"

    @task()
    def enjoy_food():
        return "Excellent dinner"
    
    check_menu() >> select_dish() >> place_order() >> enjoy_food()
    
    check_menu() >> place_order() >> enjoy_food()

dag = restaurant_routine_example_with_decorator()
