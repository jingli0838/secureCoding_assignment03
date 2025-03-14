import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    user_input = input('Enter your name: ')
    
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    # A02:2021 - Cryptographic Failures
    # should always use the https secure-api url
    url = 'https://secure-api.com/get-data'  
    # A08:2021 - Software and Data Integrity Failures
    # should use try-except block to handdle errors properly
    data = urlopen(url).read().decode() 
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')" # 
    connection = pymysql.connect(**db_config)
    # A08:2021 - Software and Data Integrity Failures
    # sould use try-except block to handdle errors properly when execute query. 
    # If the errors are not handled properly, the process may crash.
    connection.commit()
    cursor = connection.cursor()
    cursor.execute(query) 
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
