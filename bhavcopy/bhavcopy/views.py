from django.shortcuts import render
from security.models import MarketDataInfo
from company.models import Details
from .forms import SearchCompanyForm
from company.serializers import CompanyDetailSerializer
from security.serializers import MarketDataSerializer
import zipfile
import wget
import requests
import csv


def create_security_csv():
    try:
        dataReader = csv.reader(
            open('Pd041022.csv'), delimiter=',')
    except:
        url = "https://archives.nseindia.com/archives/equities/bhavcopy/pr/PR041022.zip"
        wget.download(url, ".")
        with zipfile.ZipFile('PR041022.zip', 'r') as zip_ref:
            zip_ref.extract('Pd041022.csv', '.')

    dataReader = csv.reader(
        open('Pd041022.csv'), delimiter=',')
    i = 0
    details = [f.name for f in MarketDataInfo._meta.get_fields()][1:]
    for row in dataReader:
        i += 1
        if i > 1:
            try:
                security = MarketDataInfo.objects.get(security=row[3])
            except:
                if row[2] == " ":
                    continue

                security = {}
                for i in range(len(details)):
                    security[details[i]] = row[i]

                serializer = MarketDataSerializer(data=security)
                if serializer.is_valid():
                    serializer.save()


def create_company_csv():
    try:
        dataReader = csv.reader(
            open('EQUITY_L.csv'), delimiter=',')
    except:
        url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
        response = requests.get(url)
        with open('EQUITY_L.csv', 'w+') as csv_file:
            csv_file.write(response.text)

    dataReader = csv.reader(
        open('EQUITY_L.csv'), delimiter=',')
    i = 0
    details = [f.name for f in Details._meta.get_fields()][1:]
    for row in dataReader:
        i += 1
        if i > 1:
            try:
                company = Details.objects.get(symbol=row[0])
            except:

                company = {}
                for i in range(len(details)):
                    company[details[i]] = row[i]
                serializer = CompanyDetailSerializer(data=company)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()


def SearchCompanyView(request):
    if(len(Details.objects.all()) == 0):
        create_company_csv()
        create_security_csv()

    form = SearchCompanyForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        notation = form.cleaned_data.get("symbol")
        securities = MarketDataInfo.objects.all().filter(symbol__symbol=notation)
        security_fields = [
            f.name for f in MarketDataInfo._meta.get_fields()][1:]
        symbol_fields = [f.name for f in Details._meta.get_fields()][1:]
        symbol = Details.objects.all().filter(symbol=notation)
        form = SearchCompanyForm()
        context = {"symbol": symbol, "securities": securities,
                   "security_fields": security_fields, "symbol_fields": symbol_fields, "form": form}

    return render(request, "home.html", context=context)
