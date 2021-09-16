from flask import Flask
from flask_cors import CORS

from .health.controllers import health
from .machine_learning.controllers import ml

app = Flask(__name__)
CORS(app)
app.register_blueprint(health)
app.register_blueprint(ml)
