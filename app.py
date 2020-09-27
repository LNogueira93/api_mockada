from flask import Flask, Blueprint
from rotas.demo_api import demo_app
from flask_cors import CORS
import infra.demo_db as demo_db

app = Flask(__name__)

CORS(app)

app.register_blueprint(demo_app)

demo_db.init()

if __name__ == '__main__':
    app.run(port=5004, debug=True)