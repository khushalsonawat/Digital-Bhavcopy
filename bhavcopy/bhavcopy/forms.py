from django import forms


class SearchCompanyForm(forms.Form):
    symbol = forms.CharField(max_length=200)
