from django.db import models


class Details(models.Model):
    symbol = models.CharField(
        max_length=200,
        primary_key=True,
        null=False,
        blank=False
    )
    company_name = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    series = models.CharField(max_length=2)
    listing_date = models.CharField(max_length=50)
    paid_up_value = models.IntegerField()
    market_lot = models.IntegerField(default=1)
    isin_number = models.CharField(max_length=15)
    face_value = models.IntegerField()
