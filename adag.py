from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Set the start date for the DAG
start_date = datetime(2024, 6, 7)

# Define the default arguments for the DAG
default_args = {
    'owner': 'admin',
    'start_date': start_date,
    'retry_delay': timedelta(seconds=30),
}

# Define the DAG
with DAG('a_nyt_scraper', default_args=default_args, schedule_interval='*/5 * * * *', catchup=False) as dag:

    # Task 0: Start message
    t0 = BashOperator(
        task_id="starting",
        bash_command="echo 'Starting the script'",
    )

    # Task 1: Run the Python script to scrape data
    t1 = BashOperator(
        task_id="getting_data_from_url",
        bash_command="source ~/python_env/python_env/bin/activate && python /home/cagri/airflow/dags/main.py"
    )

    # Task 2: End message
    t2 = BashOperator(
        task_id="end",
        bash_command="echo 'Script has finished running'",
    )

    # Define task dependencies
    t0 >> t1 >> t2

