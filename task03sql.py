 
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

 
app = Flask(__name__)

 
def connect_to_database():
    return sqlite3.connect("database.db")

 
def create_table():
    conn = connect_to_database()  
    cursor = conn.cursor()  
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            middle_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            contact INT,
            student_number INT
        )
    ''')  
    conn.commit()  
    conn.close()  

 
def insert_data(first_name, middle_name, last_name, contact, student_number):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_data (first_name, middle_name, last_name, contact, student_number)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, middle_name, last_name, contact, student_number))
    conn.commit()
    conn.close()

 
def get_all_data():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    data = cursor.fetchall()
    conn.close()
    return data

 
@app.route("/a")
def main():
    return render_template('taskthreesql_index.html')

 
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

     
    return render_template('taskthreesql_display.html', htmldata=data)

 
@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    conn = connect_to_database()
    cursor = conn.cursor()
    if request.method == 'POST':
         
        first_name = request.form['fname']
        middle_name = request.form['midname']
        last_name = request.form['lname']
        contact = request.form['tel']
        student_number = request.form['usn']

        cursor.execute('''
            UPDATE user_data
            SET first_name=?, middle_name=?, last_name=?, contact=?, student_number=?
            WHERE id=?
        ''', (first_name, middle_name, last_name, contact, student_number, id))
        conn.commit()
        conn.close()
        return redirect(url_for('display'))
    else:
         
        cursor.execute("SELECT * FROM user_data WHERE id=?", (id,))
        data = cursor.fetchone()
        conn.close()
         
        return render_template('taskthreesql_edit.html', htmldata=data)

 
@app.route("/delete/<int:id>")
def delete(id):
    conn = connect_to_database()
    cursor = conn.cursor()
     
    cursor.execute("DELETE FROM user_data WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('display'))

 
create_table()

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
