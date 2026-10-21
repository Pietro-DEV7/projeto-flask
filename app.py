from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Olá, mundo!</p>'

@app.route('/Pietro')
def ola_pietro():
    nome = request.args.get('nome', 'Flask')
    return f'<p>Olá, {escape(nome)}!</p>'

@app.route("/<usuario/<username>")
def home_usuario(username):
    return f'<p>Olá, {escape(username)}!</p>'

@app.route("/olá/")
@app.route("/olá/<nome>")
def ola(nome=None):
  return render_template('ola.html', nome=nome)
