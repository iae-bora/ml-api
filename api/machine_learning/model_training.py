from numpy.core.fromnumeric import mean
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold
import logging

logger = logging.getLogger(__name__)


def Treinar(locais, x, y, rodada, entrada, sample):
    #Separação de treino e teste
    
    #y = dataset['destino'].str.strip()
    #x = dataset.drop(columns=['destino'])
    #y_sample = sample['destino'].str.strip()
    #x_sample = sample.drop(columns=['destino'])

    #Clusterização
    kmeans = KMeans(n_clusters=3)

    data_array = x.values

    x["clusters"] = kmeans.fit_predict(data_array)
    entrada.append(kmeans.predict([entrada]))

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, shuffle=True)


    modelo = DecisionTreeClassifier(max_depth=15)
    modelo.fit(X_train, y_train)

    #cv = StratifiedKFold(n_splits = 5, shuffle=True)
    #results = cross_validate(modelo, x, y, cv = cv, n_jobs = 3)
    #media = results ['test_score'].mean()
    #desvio_padrao = results['test_score'].std()
    #print("Accuracy com cross validation, 5 = [%.2f, %.2f]" % ((media - 2 *desvio_padrao) * 100, (media + 2 * desvio_padrao) * 100))

    previsoes_SVC = modelo.predict(X_train)
    acuracia = accuracy_score(y_train, previsoes_SVC) * 100
    #acuracia_cross = mean(results['test_score'])*100
    
    #previsoes_sample = modelo.predict(x_sample)
    #acuracia_sample = accuracy_score(y_sample, previsoes_sample) * 100

    logger.info("---------------------------------------------------------------------------------------------")
    logger.info("Rodada: " + str(rodada))
    logger.info("Treinaremos com %d elementos e testaremos com %d elementos" % (len(X_train), len(X_test)))
    logger.info("A acurácia foi de %.2f%%" % acuracia)
    #logger.info("A acurácia cross foi de %.2f%%" % acuracia_cross)
    logger.info(entrada)

    saida = modelo.predict([entrada])

    return saida, acuracia, ""

def Recomendar(dataset, resposta):

    #Clusterização
    y = dataset['destino'].str.strip()
    x = dataset.drop(columns=['destino'])

    kmeans = KMeans(n_clusters=3)
    x['Cluster'] = kmeans.fit_predict(x)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    modelo = DecisionTreeClassifier(max_depth=15)
    modelo.fit(X_train, y_train)
    previsoes_SVC = modelo.predict(X_train)
    cv = StratifiedKFold(n_splits = 5, shuffle=True)
    results = cross_validate(modelo, x, y, cv = cv, n_jobs = 3)
    acuracia_cross = mean(results['test_score'])*100

    acuracia = accuracy_score(y_train, previsoes_SVC) * 100
    logger.info("A acurácia foi de %.2f%%" % acuracia_cross)

    return modelo
