from rest_framework import serializers
from .models import MarketDataInfo


class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketDataInfo
        fields = [
            "market",
            "series",
            "symbol",
            "security",
            "prev_cl_price",
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "net_tradeval",
            "net_tradeqty",
            'ind_sec',
            "corp_ind",
            "trades",
            "high_52_wk",
            "low_52_wk",
        ]
