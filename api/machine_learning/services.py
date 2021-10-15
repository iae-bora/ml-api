import random
import pandas as pd
import logging
import os
from flask import jsonify
from imblearn.under_sampling import NearMiss
import api.machine_learning.model_training as treino



enum_saida = {
    "Parque" : 1,
    "Museu" : 2,
    "Cinema" : 3,
    "Shopping" : 4,
    "Bar" : 5,
    "Restaurante" : 6,
    "Show" : 7,
    "Biblioteca" : 8,
    "Estádio" : 9,
    "Jogos" : 10,
    "Teatro" : 11,
}

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

class Service:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def predict(self, params):
        try:
            locais_aux = params['places']
            index_dict = list(enum_saida.keys())
            print(index_dict)
            locais = []

            n = 0
            for i in locais_aux:
                print(locais_aux[n])
                locais.append(index_dict[locais_aux[n]-1])
                n = n + 1

            retornos = []
            
            lista = [
                params['id'], 
                params['musics'], 
                params['food'], 
                params['movies'], 
                params['sports'], 
                params['teams'],
                params['religion'],
                params['haveChildren'],
                params['userAge']
            ]

            self.logger.info(f'Received answers: {lista}')

            dataset = pd.read_csv(os.path.join(os.getcwd(), 'api', 'machine_learning', 'dados.csv'))
            dataset = dataset.drop(columns='Unnamed: 0')
            dataset = dataset.query("destino != 'OUTROS'")

            for i in range(params['placesCount']):
                dataset = dataset[dataset['destino'].isin(locais)]
                modelo = treino.Recomendar(dataset, lista)
                recomendacao = modelo.predict([lista])[0]
                self.logger.info(f'Recommended category: {recomendacao}')

                recomendacao_convertida = enum_saida[recomendacao]
                retornos.append(recomendacao_convertida)

                if recomendacao != 'OUTROS':
                    locais.remove(recomendacao)
            
            self.logger.info(f'List of recommendations: {retornos}')
            return jsonify(retornos), 200
            
        except Exception as e:
            self.logger.error(f'Error while processing recommendations: {e}')
            return { 'message': f'Error while processing recommendations: {str(e)}' }, 500

    def train(self):
        rodadas = []
        acuracias = []
        locais = ['CINEMA', 'RESTAURANTE', 'SHOPPING', 'PARQUE', 'SHOW', 'MUSEU', 'BIBLIOTECA', 'ESTÁDIO',  'JOGOS', 'TEATRO', 'BAR']
        dataset = pd.read_csv(os.path.join(os.getcwd(), 'api', 'machine_learning', 'dadosv1.csv'), sep = ";", encoding='ISO-8859-1')
        
        #dataset = dataset.drop(columns=['Unnamed: 0'])
        print(dataset)
        dataset = dataset.query("destino != 'OUTROS'")
        sample = dataset.sample(n=50)

        self.logger.info(f'Dataset shape: {str(dataset.shape)}')
        dataset = dataset[~dataset.isin(sample)]
        dataset = dataset.dropna()

        y = dataset['destino'].str.strip()
        x = dataset.drop(columns=['destino'])


        for rodada in range(2000):
            y = dataset['destino'].str.strip()
            x = dataset.drop(columns=['destino'])


            entrada = [random.randint(0,6), random.randint(0,5), random.randint(0,7), random.randint(0,4), random.randint(0,4), random.randint(0,5), random.randint(0,1), random.randint(15,60)]
            resposta, acuracia, acuracia_sample = treino.Treinar(locais, x, y, rodada, entrada, sample)
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

        dataset.to_csv(os.path.join(os.getcwd(), 'api', 'machine_learning', 'dados.csv'))

        return {'message': 'Model trained successfully'}, 200
