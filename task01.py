from flask import Flask, render_template, request


jamodiong = Flask(__name__)

@jamodiong.route("/")
def view_form():
    return render_template('taskone_index.html')

@jamodiong.route('/main', methods=['POST'])
def get_posts():
    if request.method == 'POST':
        pangalan = request.form['name']
        taon = int(request.form['born'])
        labog = 2023 - taon
        return render_template('taskone_display.html',sample = pangalan,kuha = labog)

if __name__ == '__main__':
    jamodiong.run(host='0.0.0.0', debug=True)
