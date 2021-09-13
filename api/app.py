from flask import Flask, Response, jsonify, request
from flask_cors import CORS

# from .errors import errors
from .health.controllers import health

app = Flask(__name__)
CORS(app)
app.register_blueprint(health)
# app.register_blueprint(errors)

# import pickle, os
# import treino_modelo as treino

# @app.route('/predict', methods=['POST'])
# def predict():
#     request_params = request.get_json(force=True)

#     try:
#         answers_list = list(request_params['answers'].values())
#         print(answers_list)

#         place_categories_list = ['CINEMA', 'RESTAURANTE', 'SHOPPING', 'PARQUE', 'SHOW', 'MUSEU', 'BIBLIOTECA', 'ESTÁDIO', 'BIBLIOTECA', 'JOGOS', 'TEATRO', 'BAR']

#         recommended_categories = []

#         for i in range(request_params['qtd_destinos']):
#             ml_model = treino.Recomendacao(place_categories_list)
#             recommended_category = ml_model.predict([answers_list])
#             recommended_categories.append(recommended_category[0].upper())
#             print(recommended_category[0].upper())
#             if recommended_category[0].upper() != 'OUTROS':
#                 place_categories_list.remove(recommended_category[0].upper())
#         saida = {'recomendacao' : recommended_categories}

#         return saida, 200
#     except:
#         return { 'message': 'Error while processing recommendations' }, 500
