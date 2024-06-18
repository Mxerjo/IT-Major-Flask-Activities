from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def connect_to_database():
    connection = psycopg2.connect(
        host="localhost",
        database="databasepostgresql",
        user="postgres",
        password="admin1234"
    )
    return connection

def create_table():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            middle_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            contact TEXT,  
            student_number TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(first_name, middle_name, last_name, contact, student_number):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_data (first_name, middle_name, last_name, contact, student_number)
        VALUES (%s, %s, %s, %s, %s)
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

@app.route("/")
def main():
    return render_template('task04postgre_index.html')

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
    return render_template('task04postgre_display.html', htmldata=data)

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
            SET first_name=%s, middle_name=%s, last_name=%s, contact=%s, student_number=%s
            WHERE id=%s
        ''', (first_name, middle_name, last_name, contact, student_number, id))
        conn.commit()
        conn.close()
        return redirect(url_for('display'))
    else:
        cursor.execute("SELECT * FROM user_data WHERE id=%s", (id,))
        data = cursor.fetchone()
        conn.close()
        return render_template('task04postgre_edit.html', htmldata=data)

@app.route("/delete/<int:id>")
def delete(id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_data WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('display'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
