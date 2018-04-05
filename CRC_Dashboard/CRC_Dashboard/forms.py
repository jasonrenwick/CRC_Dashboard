from django import forms


class FarmerIDform(forms.Form):
    farmer = forms.CharField(label='Farmer ID', max_length=4)