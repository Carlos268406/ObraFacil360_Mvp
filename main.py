from flask import Flask, render_template, request, redirect
from urllib.parse import quote

app = Flask(__name__,template_folder='app/templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])  # mantenha o nome da rota igual ao action do HTML
def enviar():
    # Captura todos os campos do formulário
    nome = request.form.get('nome')
    servico = request.form.get('servico')
    bairro = request.form.get('bairro')

    numero_whatsapp = "5511997100740"
    mensagem = f"Olá! Sou {nome}. Preciso de um orçamento para {servico} no bairro {bairro}."
    texto_codificado = quote(mensagem)

    link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={texto_codificado}"

    # 🔴 IMPORTANTE: redirecionar o usuário
    return redirect(link_whatsapp)


if __name__ == '__main__':
    app.run(debug=True)