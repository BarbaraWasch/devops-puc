from flask import Flask

# Esta função cria a nossa aplicação web
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Projeto DevOps</h1><p>Aplicação web simples para as atividades da disciplina.</p>"

    @app.route("/health")
    def health_check():
        return {"status": "ok"}, 200

    return app

# Este bloco permite executar a aplicação diretamente
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)