import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset/system_data.csv")

# Features
X = data[["CPU", "RAM", "DISK"]]

# Target
y = data["STATUS"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("ai/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")