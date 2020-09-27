from flask import Blueprint, jsonify, request, Flask, render_template
from flask_cors import CORS
from services.demo_services import \
    listar as service_listar

app = Flask(__name__)

CORS(app,resources = {r"/*": {"origins": "*", 'Access-Control-Allow-Origin': '*'}})

demo_app = Blueprint('demo_app', __name__)

BASE_ROUTE = "produtos"

@demo_app.route(f"/{BASE_ROUTE}/listar")
def listar_produtos():
    demo = service_listar()
    return jsonify(demo)
