from flask import Flask

import database
from routes.usuario_routes import usuario_bp
from routes.moradia_routes import moradia_bp



def create_app(database_url=None):
    if database_url:
        database.configure_database(database_url)
    database.init_db()

    app = Flask(__name__)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(moradia_bp)

    @app.route("/")
    def inicio():
        return "RoomHub funcionando!"

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)