# from flask import Flask, request
# from flask_cors import CORS
# import pickle, os
# from numpy.core.records import record
import api.machine_learning.model_training as treino
import random
import pandas as pd
import logging
import os
# from multiprocessing import  Pool
import numpy as np
# import matplotlib.pyplot as plt
# import threading
# from queue import Queue
# import warnings
# warnings.filterwarnings('ignore')

rodadas = []
acuracias = []
acuracias_sample = []
locais = ['CINEMA', 'RESTAURANTE', 'SHOPPING', 'PARQUE', 'SHOW', 'MUSEU', 'BIBLIOTECA', 'ESTÁDIO', 'BIBLIOTECA', 'JOGOS', 'TEATRO', 'BAR']

enum_saida = {
    "Parque" : 1,
    "Museu" : 2,
    "Cinema" : 3,
    "Shopping" : 4,
    "Bar" : 5,
    "Show" : 7,
    "Biblioteca" : 8,
    "Estádio" : 9,
    "Jogos" : 10,
    "Teatro" : 11,
}

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')

class Service:
    def __init__(self):
        # self._gerarBase()
        self.logger = logging.getLogger(__name__)
    
    def _gerarBase(self):
        locais = ['CINEMA', 'RESTAURANTE', 'SHOPPING', 'PARQUE', 'SHOW', 'MUSEU', 'BIBLIOTECA', 'ESTÁDIO', 'BIBLIOTECA', 'JOGOS', 'TEATRO', 'BAR']
        dataset = pd.read_csv("C:\\Users\\Kaique\\OneDrive\\Área de Trabalho\\TCC\dados1.csv")
        dataset = dataset.drop(columns='Unnamed: 0')

        for rodada in range(6000):
            
            entrada = [random.randint(0,6), random.randint(0,5), random.randint(0,7), random.randint(0,4), random.randint(0,4), random.randint(0,5), random.randint(0,1), random.randint(15,60)]
            resposta, acuracia  = treino.Recomendacao(locais, dataset, rodada, entrada)
            acuracias.append(acuracia)
            rodadas.append(rodada)
            entrada.append(str(resposta[0]))

            dict_entrada = {
                'genero_musical' : entrada[0],
                'comida_favorita' : entrada[1],
                'filme_favorito' : entrada[2],
                'esporte_favorito' : entrada[3],
                'time' : entrada[4],
                'religiao' : entrada[5],
                'tem_filhos' : entrada[6],
                'idade' : entrada[7],
                'destino' : entrada[9]
            }

            dataset = dataset.append(dict_entrada, ignore_index=True)
        return dataset
    
    def predict(self, params):
        try:
            retornos = []
            entrada = params['answers']

            dataset = pd.read_csv(os.path.join(os.getcwd(), 'api', 'machine_learning', 'dados.csv'))
            dataset = dataset.drop(columns='Unnamed: 0')
            dataset = dataset.query("destino != 'OUTROS'")

            lista = entrada
            print(lista)

            for i in range(params['qtd_destinos']):
                dataset = dataset[dataset['destino'].str.upper().isin(locais)]
                modelo = treino.Recomendar(dataset, entrada)
                recomendacao = modelo.predict([lista])[0]
                recomendacao_convertida = enum_saida[recomendacao]
                retornos.append(recomendacao_convertida)

                if recomendacao.upper() != 'OUTROS':
                    locais.remove(recomendacao.upper())

            return {'recomendacoes': retornos}, 200
        except Exception as e:
            self.logger.error(e)
            return { 'message': 'Error while processing recommendations' }, 500

    def train():
        dataset = pd.read_csv(os.path.join(os.getcwd(), 'api', 'machine_learning', 'dados_treino.csv'))
        dataset = dataset.drop(columns='Unnamed: 0')
        dataset = dataset.query("destino != 'OUTROS'")
        sample = dataset.sample(n=50)
        print(dataset.shape)
        print(dataset)
        dataset = dataset[~dataset.isin(sample)]
        dataset = dataset.dropna()

        for rodada in range(20000):
            
            entrada = [random.randint(0,6), random.randint(0,5), random.randint(0,7), random.randint(0,4), random.randint(0,4), random.randint(0,5), random.randint(0,1), random.randint(15,60)]
            resposta, acuracia, acuracia_sample = treino.Treinar(locais, dataset, rodada, entrada, sample)
            acuracias.append(acuracia)

            rodadas.append(rodada)
            entrada.append(str(resposta[0]))

            dict_entrada = {
                'genero_musical' : entrada[0],
                'comida_favorita' : entrada[1],
                'filme_favorito' : entrada[2],
                'esporte_favorito' : entrada[3],
                'time' : entrada[4],
                'religiao' : entrada[5],
                'tem_filhos' : entrada[6],
                'idade' : entrada[7],
                'destino' : entrada[9]
            }
            dataset = dataset.append(dict_entrada, ignore_index=True)

        dataset.to_csv("dados.csv")


# app = Flask(__name__)
# CORS(app)

# @app.route('/', methods=['GET'])
# def home():
#     return { 'message': 'Working correctly!' }

# @app.route('/predict', methods=['POST'])
# def predict():
#     entrada = request.get_json(force=True)['answers']

#     lista = list(entrada.values())
#    # print(lista)

#     locais = ['CINEMA', 'RESTAURANTE', 'SHOPPING', 'PARQUE', 'SHOW', 'MUSEU', 'BIBLIOTECA', 'ESTÁDIO', 'BIBLIOTECA', 'JOGOS', 'TEATRO', 'BAR']

#     for i in range(entrada['qtd_destinos']):
#         modelo = treino.Recomendacao(locais)
#         recomendacao = modelo.predict([lista])
#         retornos.append(recomendacao[0].upper())
#         #print(recomendacao[0].upper())
#         if recomendacao[0].upper() != 'OUTROS':
#             locais.remove(recomendacao[0].upper())
#     saida = {'recomendacao' : retornos}

#     return saida

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)

# def gerarBase():
#     locais = ['CINEMA', 'RESTAURANTE', 'SHOPPING', 'PARQUE', 'SHOW', 'MUSEU', 'BIBLIOTECA', 'ESTÁDIO', 'BIBLIOTECA', 'JOGOS', 'TEATRO', 'BAR']
#     dataset = pd.read_csv("C:\\Users\\Kaique\\OneDrive\\Área de Trabalho\\TCC\dados1.csv")
#     dataset = dataset.drop(columns='Unnamed: 0')

#     #plt.ion()
#     for rodada in range(6000):
        
#         entrada = [random.randint(0,6), random.randint(0,5), random.randint(0,7), random.randint(0,4), random.randint(0,4), random.randint(0,5), random.randint(0,1), random.randint(15,60)]
#         resposta, acuracia  = treino.Recomendacao(locais, dataset, rodada, entrada)
#         acuracias.append(acuracia)
#         rodadas.append(rodada)
#         entrada.append(str(resposta[0]))

#         dict_entrada = {
#             'genero_musical' : entrada[0],
#             'comida_favorita' : entrada[1],
#             'filme_favorito' : entrada[2],
#             'esporte_favorito' : entrada[3],
#             'time' : entrada[4],
#             'religiao' : entrada[5],
#             'tem_filhos' : entrada[6],
#             'idade' : entrada[7],
#             'destino' : entrada[9]
#         }

#         dataset = dataset.append(dict_entrada, ignore_index=True)

#         if rodada == 5999:
#             plt.plot(rodadas, acuracias)
#             plt.xlabel("Rodada de treino")
#             plt.ylabel("Acurácia")
#             plt.draw()
#             plt.show()
#     return dataset



# if __name__ == '__main__':
#     dataset = gerarBase()
#     dataset.to_csv("C:\\Users\\Kaique\\OneDrive\\Área de Trabalho\\TCC\\dados.csv")