import pickle
import pandas as pd

with open("ai/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_failure(cpu, ram, disk):

    prediction = model.predict(
        pd.DataFrame(
            [[cpu, ram, disk]],
            columns=["CPU", "RAM", "DISK"]
        )
    )

    return prediction[0]