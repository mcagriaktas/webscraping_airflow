from LoggingWrapper import loggingwrapper
import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime

# PostgreSQL connection details
postgres_info = {
    "ip": "172.80.0.150",
    "port": 5432,
    "database": "mydb",
    "username": "cagri",
    "password": "3541"
}

@loggingwrapper
def connect_database():
    """
    This function establishes a connection to the PostgreSQL database using the connection details provided.
    
    Returns:
        connection: A psycopg2 connection object if successful.
    """
    connection = psycopg2.connect(
        host=postgres_info['ip'],
        port=postgres_info['port'],
        database=postgres_info['database'],
        user=postgres_info['username'],
        password=postgres_info['password']
    )
    return connection

@loggingwrapper
def insert_data_to_db(connection, articles):
    """
    This function inserts the scraped articles into the PostgreSQL database.
    
    Args:
        connection: A psycopg2 connection object to the database.
        articles: A list of dictionaries where each dictionary contains article data (Title, Link, Info, Author, Date).
    """
    cursor = connection.cursor()
    for article in articles:
        cursor.execute("""
            INSERT INTO nyt_news (Title, Link, Info, Author, Date) 
            VALUES (%s, %s, %s, %s, %s)
        """, (article['Title'], article['Link'], article['Info'], article['Author'], article['Date']))
    connection.commit()

@loggingwrapper
def scrape_nyt_technology(last_page: int):
    """
    This function scrapes the New York Times Technology section for articles across multiple pages.
    
    Args:
        last_page: The last page number to scrape.

    Returns:
        articles: A list of dictionaries where each dictionary contains article data (Title, Link, Info, Author, Date).
    """
    articles = []
    for page in range(1, last_page + 1):
        url = f"https://www.nytimes.com/international/section/technology?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for item in soup.find_all('li', class_='css-18yolpw'):
            title_tag = item.find('a', class_=any)
            if title_tag:
                title = title_tag.get_text()
                link = title_tag['href']
                full_link = f"https://www.nytimes.com{link}"
                info = item.find('p', class_=any).get_text() if item.find('p', class_=any) else "No additional information available"
                author = item.find('span', class_=any).get_text().strip() if item.find('span', class_=any) else "No author listed"
                try:
                    if "interactive" in full_link:
                        date_str = full_link.split('/')[4:7]
                    else:
                        date_str = full_link.split('/')[3:6]
                    date = datetime.strptime('/'.join(date_str), '%Y/%m/%d').date()
                except (ValueError, IndexError):
                    date = None
                articles.append({"Title": title, "Link": full_link, "Info": info, "Author": author, "Date": date})
    return articles

if __name__ == "__main__":
    last_page = 10
    articles = scrape_nyt_technology(last_page)
    if articles:
        connection = connect_database()
        if connection:
            insert_data_to_db(connection, articles)
            connection.close()
