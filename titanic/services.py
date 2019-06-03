# Domain Model - Business Logic regarding predictions
import dill as pickle
import os
from Insightish.settings import BASE_DIR
from .modeling import PreProcessing


def predict(data):
    with open(os.path.join(BASE_DIR, 'media\model_v1.pk'), 'rb') as file:
        model = pickle.load(file)
    prediction = model.predict(data)
    prediction_confidence = model.predict_proba(data)
    return prediction[0], prediction_confidence
