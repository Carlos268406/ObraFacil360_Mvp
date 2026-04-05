from flask import Flask, render_template, request, redirect
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    # Agora os nomes dos campos batem com o HTML
    titulo = request.form.get('nome')
    bairro = request.form.get('bairro')

    numero_whatsapp = "5511997100740"
    # Monta a mensagem com os dados recebidos
    mensagem = f"{titulo} - {bairro}"
    texto_codificado = quote(mensagem)

    link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={texto_codificado}"
    return redirect(link_whatsapp)

if __name__ == '_main_':
    app.run(debug=True)
