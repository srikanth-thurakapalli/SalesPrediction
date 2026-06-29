import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# -----------------------------
# Load Dataset
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(BASE_DIR, "dataset", "superstore.csv")

df = pd.read_csv(dataset_path, encoding="latin1")

print("Dataset Loaded Successfully")
print(df.shape)

# -----------------------------
# Select Required Columns
# -----------------------------

df = df[
    [
        "Order Date",
        "Ship Mode",
        "Segment",
        "City",
        "State",
        "Region",
        "Category",
        "Sub-Category",
        "Quantity",
        "Discount",
        "Sales"
    ]
]

# -----------------------------
# Date Processing
# -----------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Day"] = df["Order Date"].dt.day

df.drop("Order Date", axis=1, inplace=True)

# -----------------------------
# Features & Target
# -----------------------------

X = df.drop("Sales", axis=1)
y = df["Sales"]

# -----------------------------
# Column Types
# -----------------------------

categorical_features = [
    "Ship Mode",
    "Segment",
    "City",
    "State",
    "Region",
    "Category",
    "Sub-Category"
]

numeric_features = [
    "Quantity",
    "Discount",
    "Year",
    "Month",
    "Day"
]

# -----------------------------
# Preprocessor
# -----------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numeric_features
        )
    ]
)

# -----------------------------
# Pipeline
# -----------------------------

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)

# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train
# -----------------------------

pipeline.fit(X_train, y_train)

print("Model Trained Successfully")

# -----------------------------
# Prediction
# -----------------------------

y_pred = pipeline.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("-" * 30)
print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R2   : {r2:.4f}")

# -----------------------------
# Save Model
# -----------------------------

model_path = os.path.join(BASE_DIR, "ml", "pipeline.pkl")

joblib.dump(pipeline, model_path)

print("\nPipeline Saved Successfully")
print(model_path)