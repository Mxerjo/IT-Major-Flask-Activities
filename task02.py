from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function siya nga mo connect sa database
def connect_to_database():
    return sqlite3.connect("database.db")

# Function ni siya nga mo create sa user_data table sa atong database if wala siya ga exist
def create_table():
    conn = connect_to_database()  # Conn Mao ni siya ang koneksyon sa database
    cursor = conn.cursor() # Cursor mao ni siya ang makipag interact sa conn
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            middle_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            contact INT,
            student_number INT
        )
    ''')# Cursor Execute diri nimo gi excute sql commands ug queries para sa database 
    conn.commit() # Commit is imake sure niya na ang imong gi insert na data is masaved sa database  
    conn.close() 

# Function siya para maka insert tag data sa database 
def insert_data(first_name, middle_name, last_name, contact, student_number):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_data (first_name, middle_name, last_name, contact, student_number)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, middle_name, last_name, contact, student_number))
    conn.commit()
    conn.close()

# Function para ma makuha or fetch tanan data nato gikan sa database 
def get_all_data():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def main():
    return render_template('tasktwo_index.html')

@app.route("/home", methods=['POST', 'GET'])
def display():
    if request.method == 'POST':
        first_name = request.form['fname']
        middle_name = request.form['midname']
        last_name = request.form['lname']
        contact = request.form['tel']
        student_number = request.form['usn']

        # diri nata mag insert ug data sa database 
        insert_data(first_name, middle_name, last_name, contact, student_number)

    # diri gikuha or fetch tanan data gikan sa atong database 
    data = get_all_data()

    return render_template('tasktwo_display.html', data=data)

# Create sa user_data table sa atong database if wala siya ga exist
create_table()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
