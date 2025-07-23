# AgriAutoML Crop Yield Prediction using Vertex AI

This project demonstrates how to build a crop yield prediction system using AutoML in Google Vertex AI.

## 📦 Structure
- `data/crop_yield_data.csv`: Sample tabular dataset
- `notebook.ipynb`: Vertex AI Studio notebook for training and deploying AutoML model
- `cloud_function/`: Code to expose model as REST API using Cloud Functions

## 🚀 Steps
1. Upload dataset to GCS:
   ```bash
   gsutil cp data/crop_yield_data.csv gs://your-bucket-name/datasets/
   ```

2. Open and run the `notebook.ipynb` in Vertex AI Studio

3. Replace placeholders like `your-project-id` and `your-bucket-name`

4. Deploy the Cloud Function:
   ```bash
   gcloud functions deploy predict_yield \
     --runtime python310 \
     --trigger-http \
     --allow-unauthenticated \
     --entry-point predict \
     --source cloud_function
   ```

5. Test the API:
   ```bash
   curl -X POST https://REGION-PROJECT.cloudfunctions.net/predict_yield \
     -H "Content-Type: application/json" \
     -d '{"soil_type":"loam","rainfall":300,"temperature":27,"ph":6.5,"crop_type":"wheat"}'
   ```
