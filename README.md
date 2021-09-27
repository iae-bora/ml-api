# IAe, Bora? ML API
<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/python-3.7-blue.svg" alt="Python 3.7" />
</a>

API developed in Python which predicts the categories of places that an user should visit based on his answers. This API runs K-Means and Decision Tree Classifier as machine learning models to predict the output.

## ⚒️ Technologies
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Scikit-learn](https://scikit-learn.org/stable/)

## :man_technologist: Machine learning models
- [K-Means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

## :computer: Running locally
1. Install the dependencies
```
$ pip install -r requirements.txt
```
2. Run the application
```
$ python wsgi.py
```
3. The application will start running in **localhost:8080**.

## :whale: Running with Docker
1. Run the following commands on terminal
```
$ docker build -t <CONTAINER-NAME>:latest .
$ docker run -p 8080:8080 <CONTAINER-NAME>:latest
```
2. The application will start running in **localhost:8080**.
