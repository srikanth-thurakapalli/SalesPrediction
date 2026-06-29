from django.db import models


class Prediction(models.Model):
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    segment = models.CharField(max_length=100)
    ship_mode = models.CharField(max_length=100)

    quantity = models.IntegerField()
    discount = models.FloatField()

    predicted_sales = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - ₹{self.predicted_sales:.2f}"