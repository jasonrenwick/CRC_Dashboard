from django.shortcuts import render
from dashboard.models import Farmerscore


def homepage(request):
    industry = Farmerscore.objects.filter(farmerID=0000)
    context = {
            'industry': industry,
            }
    return render(request, "homepage.html", context)


def dashboard(request):
    return render(request, "dashboard.html")
