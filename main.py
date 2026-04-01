from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solicitar')
def solicitar():
    return "<h2>Conte sobre sua obra</h2>"


if __name__ == "__main__":
    app.run(debug=True)