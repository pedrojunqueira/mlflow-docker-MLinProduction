import requests

url = "http://0.0.0.0:5553/invocations"

payload = "{\n    \"columns\": [\n        \"alcohol\",\n        \"chlorides\",\n        \"citric acid\",\n        \"density\",\n        \"fixed acidity\",\n        \"free sulfur dioxide\",\n        \"pH\",\n        \"residual sugar\",\n        \"sulphates\",\n        \"total sulfur dioxide\",\n        \"volatile acidity\"\n    ],\n    \"data\": [\n        [\n            12.8,\n            0.029,\n            0.48,\n            0.98,\n            6.2,\n            29,\n            3.33,\n            1.4,\n            0.39,\n            75,\n            0.66\n        ]\n    ]\n}"
headers = {
  'Content-Type': 'application/json; format=pandas-split'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)