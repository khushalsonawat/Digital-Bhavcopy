from django.db import models
from company.models import Details


class MarketDataInfo(models.Model):
    market = models.CharField(
        max_length=1)
    series = models.CharField(
        max_length=2)
    symbol = models.ForeignKey(
        Details,
        to_field="symbol",
        on_delete=models.CASCADE
    )
    security = models.CharField(
        max_length=200)
    prev_cl_price = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=2)
    open_price = models.DecimalField(
        null=False, max_digits=7, decimal_places=2, blank=False)
    high_price = models.DecimalField(
        null=False, max_digits=7, decimal_places=2, blank=False)
    low_price = models.DecimalField(
        null=False, max_digits=7, decimal_places=2, blank=False)
    close_price = models.DecimalField(
        null=False, max_digits=7, decimal_places=2, blank=False)
    net_tradeval = models.CharField(max_length=15)
    net_tradeqty = models.CharField(max_length=15)
    ind_sec = models.CharField(max_length=5)
    corp_ind = models.CharField(max_length=5, null=True, blank=True)
    trades = models.IntegerField()
    high_52_wk = models.DecimalField(
        null=False, max_digits=7, decimal_places=2, blank=False)
    low_52_wk = models.DecimalField(
        null=False, max_digits=7, decimal_places=2, blank=False)

    def __str__(self):
        return self.security
