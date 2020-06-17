# Serving a mlflow MLmodel server on Docker

This repository is a simple example on how to run a server using [mlflow](mlflow.org) to put a Machine Learning model to production.

"MLflow’s core philosophy is to put as few constraints as possible on your workflow: it is designed to work with any machine learning library, determine most things about your code by convention, and require minimal changes to integrate into an existing codebase. At the same time, MLflow aims to take any codebase written in its format and make it reproducible and reusable by multiple data scientists. On this page, we describe a typical ML workflow and where MLflow fits in." from [mlflow docs](https://mlflow.org/docs/latest/concepts.html)

The model was trained and "packed" into a model using mlflow [Python API](https://mlflow.org/docs/latest/python_api/index.html)

The beauty of mlflow is that while you go about running your team Machine Learning workflow it is possible to Tack, Package and then put models into production.

This example I demonstrate putting to production a mlflow Model into production in a server that can receive requests and return prediction.

The model was trained using sklearn on the winequality-red dataset which was provided on the mlflow [tutorial](https://mlflow.org/docs/latest/tutorials-and-examples/tutorial.html)


## Usage

```bash
git clone https://github.com/pedrojunqueira/mlflow-docker-MLinProduction.git
cd mlflow-docker-MLinProduction
```

Then build the image and put up the container 

```bash
docker-compose up --build
```

then the container will be running on the host machine on `http://0.0.0.0:5000/invocations` as a `POST` route

to test the server use this Python script to make a post request and receive a prediction response

```python
import requests

url = "http://0.0.0.0:5553/invocations"

payload = "{\n    \"columns\": [\n        \"alcohol\",\n        \"chlorides\",\n        \"citric acid\",\n        \"density\",\n        \"fixed acidity\",\n        \"free sulfur dioxide\",\n        \"pH\",\n        \"residual sugar\",\n        \"sulphates\",\n        \"total sulfur dioxide\",\n        \"volatile acidity\"\n    ],\n    \"data\": [\n        [\n            12.8,\n            0.029,\n            0.48,\n            0.98,\n            6.2,\n            29,\n            3.33,\n            1.4,\n            0.39,\n            75,\n            0.66\n        ]\n    ]\n}"
headers = {
  'Content-Type': 'application/json; format=pandas-split'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)

```

file is conviniently on the root of this repo which you can run with the following command

```bash
$ python request_serving_model.py
>>[5.662042399588496] 
```

to stop the container

```bash
docker-compose down
```