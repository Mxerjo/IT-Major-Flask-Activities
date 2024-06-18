from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template ('actone_main.html')

@app.route("/home")
def home():
    return render_template ('actone_home.html')

@app.route("/profile")
def profile():
    return render_template ('actone_profile.html')
      
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


  
