from flask import Flask, render_template, request 
from markupsafe import escape

jamodiong = Flask(__name__)


@jamodiong.route("/")
def view_form():
        return render_template ('acttwo_main.html')

@jamodiong.route('/handle_post', methods =['POST'])
def handle_post():
    if request.method == 'POST':
        fnum = int(request.form['fnum'])
        snum = int(request.form['snum'])
        add = fnum + snum
        diff = fnum - snum
        mul = fnum * snum
        div = fnum / snum

        return render_template('acttwo_main.html', add = add, diff = diff, mul = mul, div = div)
    else:
        return render_template('acttwo_display.html')
    
 

if __name__ == '__main__':
    jamodiong.run(host='0.0.0.0',debug=True)    
