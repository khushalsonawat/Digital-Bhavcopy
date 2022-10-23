from rest_framework import serializers
from .models import Details


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ["symbol",
                  "company_name",
                  "series",
                  "listing_date",
                  "paid_up_value",
                  "market_lot",
                  "isin_number",
                  "face_value"]
