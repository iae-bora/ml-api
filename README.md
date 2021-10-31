<h1 align='center'>
  <img width=200 height=100 src="./.github/logo.png" alt="IAe, Bora?" title="IAe, Bora?"/>
</h1>

<p align="center">
  <a href="#book-about">About</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%EF%B8%8F-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#man_technologist-machine-learning-models">Machine learning models</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#cityscape-solution-architecture">Solution architecture</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#computer-running-locally">Running locally</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#whale-running-with-docker">Running with Docker</a>
</p>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Python&message=3.7&color=00A1BF&labelColor=000000" alt="Python 3.7" />
</p>

## :book: About

API developed in Python which predicts the categories of places that an user should visit based on his answers. This API runs K-Means and Decision Tree Classifier as machine learning models to predict the output.

## ⚒️ Technologies
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Scikit-learn](https://scikit-learn.org/stable/)

## :man_technologist: Machine learning models
- [K-Means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

## :cityscape: Solution architecture
This repository is represented by the number 3 in the architecture, if you want to view the other repositories of the solution, click on one of the items below:

<p align="center">
  <img src="architecture.png"/>
</p>

- [(1) Web Crawler](https://github.com/iae-bora/abc-tourism-crawler)
- [(4) Back-End](https://github.com/iae-bora/back-end)
- [(5) Front-End](https://github.com/iae-bora/front-end)
- [(6) Mobile](https://github.com/iae-bora/mobile)

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
