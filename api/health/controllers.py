from flask import Blueprint


health = Blueprint("health", __name__, url_prefix="/health")


@health.route("/")
def index():
    return { 'message': 'Working correctly!' }, 200
