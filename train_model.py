import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

# Training data
X = np.array([[-10], [-5], [-1], [1], [5], [10]])
y = np.array([0, 0, 0, 1, 1, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")