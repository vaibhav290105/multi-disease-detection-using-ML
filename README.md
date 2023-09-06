# Multi-Disease Prediction Using ML

This project develops ML models to predict diabetes, heart disease, Parkinson's disease, and chronic kidney disease.

## Model Training

The `update_models.py` script trains the models on the latest data and saves them using Pickle:

```python
python update_models.py
```

It trains the following models and saves them to `/Models`:

* Logistic Regression
* Random Forest
* Support Vector Machine
* K-Nearest Neighbors
* Decision Tree
* Gaussian Naive Bayes

## Predictions

The `main.py` script launches a Streamlit UI to interactively make predictions using the trained models:

python
streamlit run main.py

Users can input patient parameters through the UI and get real-time predictions for the risk of different diseases.