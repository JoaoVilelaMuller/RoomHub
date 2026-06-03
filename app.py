from flask import Flask
from routes.usuario_routes import usuario_bp
from routes.moradia_routes import moradia_bp

app = Flask(__name__)

@app.route("/")
def inicio():
    return "RoomHub funcionando!"

app.register_blueprint(usuario_bp)
app.register_blueprint(moradia_bp)

if __name__ == "__main__":
    app.run(debug=True)