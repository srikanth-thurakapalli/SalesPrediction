import os
import joblib
import pandas as pd

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load trained pipeline
pipeline = joblib.load(os.path.join(BASE_DIR, "ml", "pipeline.pkl"))

sample = pd.DataFrame({
    "Ship Mode": ["Second Class"],
    "Segment": ["Consumer"],
    "City": ["Henderson"],
    "State": ["Kentucky"],
    "Region": ["South"],
    "Category": ["Furniture"],
    "Sub-Category": ["Chairs"],
    "Quantity": [3],
    "Discount": [0],
    "Year": [2016],
    "Month": [11],
    "Day": [8]
})

# Predict
prediction = pipeline.predict(sample)

print("=" * 40)
print("Predicted Sales:", round(prediction[0], 2))
print("=" * 40)