""" 
vv === Etapas e passo a passo ===
    
1. Hashzap
2. botao de iniciar chat
3. popup para entrar no chat
4. quando entrar no chat: (aparece para todo mundo)
    a mensagem que você entrou no chat
    o campo e o botão de enviar mensagem
5. a cada mensagem que você envia (aparece para todo mundo)
    Nome: Texto da Mensagem
 """

# vv === Código ===

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = (
    "papaodkpfplfvmpbssnvdopkpfv"  # Usando SECRET_KEY para segurança
)
app.debug = True  # settando o debug mode
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, debug=True, host="localhost")  # roda com o debug mode habilitado
    
