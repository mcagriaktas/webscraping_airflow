# webscraping_airflow

Hello, I deployed a project for web scraping New York Times Technology news. We're sending requests to the website and retrieving data using Python and BeautifulSoup. Then, we'll insert our data into PostgreSQL, but we're using SQL in DBeaver for database management. Our data is being fetched every 5 minutes with Airflow.

Tools: 
1. Python (Beautifulsoup) - (local)
2. PostgreSQL (Docker)
3. Dbeaver - (local)
4. Airflow (local)

![Screenshot from 2024-08-22 20-37-22](https://github.com/user-attachments/assets/3f49520a-767f-4cd1-aed1-313cdf124342)

I deploy all my projects in Docker, but this time I'm trying to use a local environment. So, I installed Airflow on my Ubuntu 24.04:
  1. python3 -m venv airflow_env
  2. source airflow_env/bin/activate
  3. export AIRFLOW_HOME=path_your_airflow
  4. pip install apache-airflow
  5. airflow db init
  6. airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
  7. mkdir dags
     
     ![Screenshot from 2024-08-22 20-42-06](https://github.com/user-attachments/assets/327e7fcc-3c6d-4467-8a2f-2179bee9e428)
     
  9. Start your Airflow:
      
     ![Screenshot from 2024-08-22 20-54-18](https://github.com/user-attachments/assets/300cebba-bf42-42bd-b122-20fdc62eaf6d)

How to use PostgreSQL with DBeaver:

![Screenshot from 2024-08-22 20-58-59](https://github.com/user-attachments/assets/c15f24a6-616d-4791-be99-09b617eea714)

Airflow:

![Screenshot from 2024-08-22 20-49-59](https://github.com/user-attachments/assets/2b89cb1e-57b3-42e1-93b4-17b02c85aa11)
