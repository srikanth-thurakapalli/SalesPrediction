import os
import joblib
import pandas as pd

from django.shortcuts import render
from .models import Prediction

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(
    os.path.join(BASE_DIR, "dataset", "superstore.csv"),
    encoding="latin1"
)

pipeline = joblib.load(
    os.path.join(BASE_DIR, "ml", "pipeline.pkl")
)

CATEGORIES = sorted(df["Category"].unique())
SUB_CATEGORIES = sorted(df["Sub-Category"].unique())
REGIONS = sorted(df["Region"].unique())
STATES = sorted(df["State"].unique())
CITIES = sorted(df["City"].unique())
SEGMENTS = sorted(df["Segment"].unique())
SHIP_MODES = sorted(df["Ship Mode"].unique())

def home(request):
    return render(request, "home.html")


def predict(request):

    prediction = None

    if request.method == "POST":

        category = request.POST.get("category")
        sub_category = request.POST.get("sub_category")
        region = request.POST.get("region")
        state = request.POST.get("state")
        city = request.POST.get("city")
        segment = request.POST.get("segment")
        ship_mode = request.POST.get("ship_mode")

        quantity = int(request.POST.get("quantity"))
        discount = float(request.POST.get("discount"))

        # Today's date (or you can let the user select it)
        from datetime import datetime
        today = datetime.now()

        input_df = pd.DataFrame({
            "Ship Mode": [ship_mode],
            "Segment": [segment],
            "City": [city],
            "State": [state],
            "Region": [region],
            "Category": [category],
            "Sub-Category": [sub_category],
            "Quantity": [quantity],
            "Discount": [discount],
            "Year": [today.year],
            "Month": [today.month],
            "Day": [today.day]
        })

        prediction = float(pipeline.predict(input_df)[0])

        Prediction.objects.create(
            category=category,
            sub_category=sub_category,
            region=region,
            state=state,
            city=city,
            segment=segment,
            ship_mode=ship_mode,
            quantity=quantity,
            discount=discount,
            predicted_sales=prediction
        )

    return render(
        request,
        "predict.html",
        {
            "prediction": prediction,
            "categories": CATEGORIES,
            "sub_categories": SUB_CATEGORIES,
            "regions": REGIONS,
            "states": STATES,
            "cities": CITIES,
            "segments": SEGMENTS,
            "ship_modes": SHIP_MODES,
        },
    )


def history(request):

    predictions = Prediction.objects.order_by("-created_at")

    return render(
        request,
        "history.html",
        {
            "predictions": predictions
        }
    )