import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Prediction function
def predict_number(number):

    prediction = model.predict(np.array([[number]]))[0]

    if prediction == 1:
        return "Positive Number"
    else:
        return "Negative Number"