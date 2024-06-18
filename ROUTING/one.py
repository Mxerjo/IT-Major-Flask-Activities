from flask import Flask, render_template

marjore = Flask(__name__)

@marjore.route("/one")
def isa():
    return render_template('uno.html')

@marjore.route("/two")
def dalawa():
    return render_template('duha.html')

@marjore.route("/three")
def tatlo():
    return render_template('tulo.html')

@marjore.route("/four")
def apat():
    return render_template('upat.html')

@marjore.route("/five")
def lima():
    return render_template('limaa.html')

if __name__ == '__main__':
    marjore.run(host='0.0.0.0',debug=True)