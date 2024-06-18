from flask import Flask,render_template,request,redirect,url_for
import sqlite3

jamodiong = Flask(__name__)

def db_conn():
    return sqlite3.connect("db_name.db")

def db_table():
        conn = db_conn()
        cursor = conn.cursor()
        conn.execute ('''
                CREATE TABLE IF NOT EXISTS tbl_name(
                tbl_id INTEGER PRMARY KEY,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                ''')
            )
        conn.commit()
        conn.close

def insert_data(firstname,lastname):
        conn = db_conn()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tbl_name(firstname,lastname)
            VALUES (?,?)
            ''',(firstname,lastname))
            conn.commit()
            conn.close()

def all_data():
    con = db_conn()
    curosr = conn.cursor
    cursor.execute("SELECT * FROM tbl_name)
    mydata = cursor.fetchall()
                   conn.close()
                   return mydata

@jamodiong.route("/")
def main():
    if request method == 'POST:

        firstname = request.form['fname']
        lastname = request.form['lname']

            insert_data(firstname.lastname)
    mydata = all_data()
    return render_template('display.html'),htmldata=data)

     


if __name__ == '__main__':
    jamodiong.run(host='0.0.0.0',debug=True) 
