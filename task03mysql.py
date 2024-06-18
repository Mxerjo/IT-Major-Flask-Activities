
from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'databasemysql',
}
 
def connect_db():
    return mysql.connector.connect(**db_config)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            middle_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            contact INT(20) NOT NULL,
            student_number INT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(first_name, middle_name, last_name, contact, student_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_data (first_name, middle_name, last_name, contact, student_number)
        VALUES (%s, %s, %s, %s, %s)
    ''', (first_name, middle_name, last_name, contact, student_number))
    conn.commit()
    conn.close()

@app.route("/")
def main():
    return render_template('taskthreemysql_index.html')

@app.route("/home", methods=['POST', 'GET'])
def display():
    if request.method == 'POST':
        
        first_name = request.form['fname']
        middle_name = request.form['midname']
        last_name = request.form['lname']
        contact = request.form['tel']
        student_number = request.form['usn']

        
        insert_data(first_name, middle_name, last_name, contact, student_number)

 
    data = get_all_data()
    
    return render_template('taskthreemysql_display.html', htmldata=data)


def get_all_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    data = cursor.fetchall()
    conn.close()
    return data


if __name__ == '__main__':
   
    create_table()
   
    app.run(host='0.0.0.0', debug=True)
