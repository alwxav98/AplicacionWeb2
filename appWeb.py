from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', ViewData={"Title": "Aplicacion Web 2"})

if __name__ == "__main__":
    app.run(debug=True)