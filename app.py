from flask import Flask
from config import Config
from routes.home import home_bp
from routes.chat import chat_bp
from routes.lieux import lieux_bp
from routes.itineraires import itineraires_bp

app = Flask(__name__)
app.config.from_object(Config)

# Enregistrement des blueprints
app.register_blueprint(home_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(lieux_bp)
app.register_blueprint(itineraires_bp)

if __name__ == "__main__":
    app.run(debug=True)