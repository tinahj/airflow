from __future__ import annotations
import datetime
import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.sdk import DAG


with DAG(
    dag_id="dags_bash_operator", #파일명과 dag id를 직관적으로 일치시키는 게 좋음
    schedule="0 0 * * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"), #시작날짜
    catchup=False, #현 시점에서 시작날짜 사이의 Dag을 돌릴것인지(근데 돌리면 한번에 돌려져서 주의 필요)
) as dag:
    
    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1", #객체명과 task_id 일치시키는 게 좋음
        bash_command="echo whoami", #echo = print
    )

    bash_t2 = BashOperator(
    task_id="bash_t2",
    bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2 #task 수행 순서