from django.shortcuts import render
from dashboard.models import Farmerscore


def homepage(request):
    industry = Farmerscore.objects.filter(farmerID=1234)
    A_score = float(industry[0].A1) + float(industry[0].A2) + float(industry[0].A3) + float(industry[0].A4) + float(industry[0].A5)
    A_score = A_score / 5
    context = {
            'A_score': A_score,
            }
    return render(request, "homepage.html", context)


def dashboard(request):
    return render(request, "dashboard.html")
