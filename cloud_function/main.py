from flask import Flask, request
from google.cloud import aiplatform

app = Flask(__name__)
aiplatform.init(project="your-project-id", location="us-central1")
endpoint = aiplatform.Endpoint(endpoint_name="your-endpoint-id")

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    prediction = endpoint.predict([payload])
    return {"predicted_yield": prediction.predictions[0]}