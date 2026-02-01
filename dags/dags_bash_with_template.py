from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_with_template",
    schedule = "10 0 * * *",
    start_date = pendulum.datetime(2003, 3, 1, tz="Asia/Seoul"),
    catchup = False
) as dag:
    bash_t1 = BashOperator(
        task_id = 'bash_t1',
        bash_command = 'echo "data_interval_end : {{data_interval_end}} "'
    )

    bash_t2 = BashOperator(
        task_id = 'bash_t2',
        env={
            'START_DATE' : '{{data_inerval_start | ds}}', #ds:YYY-MM-DD 형태 10자리 출력
            'END_DATE' : '{{data_interval_end | ds}}'
        },
        bash_command = 'echo $START_DATE && echo $END_DATE' #&& : 앞에 있는 COMMAND($START_DATE) 성공하면 뒤에 COMMAND도 실행
    )

    bash_t1 >> bash_t2