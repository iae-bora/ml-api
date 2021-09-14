from flask import Blueprint, request
from api.machine_learning.services import Service

ml = Blueprint("ml", __name__)

ml_service = Service()

@ml.route("/predict", methods=["POST"])
def predict():
    request_params = request.get_json(force=True)
    if request_params is None:
        return { 'message': 'Empty parameters received'}, 400
    
    return ml_service.predict(request_params)
