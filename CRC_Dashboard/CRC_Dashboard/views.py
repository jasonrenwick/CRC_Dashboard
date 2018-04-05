from django.shortcuts import render
from dashboard.models import Farmer_a_score
from dashboard.models import Farmer_b_score
from dashboard.models import a_Element
from dashboard.models import b_Element
from dashboard.models import Farmer
from django.db.models import Avg
import numpy

def homepage(request):
    industry = Farmer_a_score.objects.aggregate(Avg('A1'))
    A1_Avg = industry['A1__avg']

    industry = Farmer_a_score.objects.aggregate(Avg('A2'))
    A2_Avg = industry['A2__avg']

    industry = Farmer_a_score.objects.aggregate(Avg('A3'))
    A3_Avg = industry['A3__avg']

    industry = Farmer_a_score.objects.aggregate(Avg('A4'))
    A4_Avg = industry['A4__avg']

    industry = Farmer_a_score.objects.aggregate(Avg('A5'))
    A5_Avg = industry['A5__avg']

    A_avg = A1_Avg + A2_Avg + A3_Avg + A4_Avg + A5_Avg
    A_avg = A_avg / a_Element.objects.count()

    industry = Farmer_b_score.objects.aggregate(Avg('B1'))
    B1_Avg = industry['B1__avg']

    industry = Farmer_b_score.objects.aggregate(Avg('B2'))
    B2_Avg = industry['B2__avg']

    industry = Farmer_b_score.objects.aggregate(Avg('B3'))
    B3_Avg = industry['B3__avg']

    industry = Farmer_b_score.objects.aggregate(Avg('B4'))
    B4_Avg = industry['B4__avg']

    industry = Farmer_b_score.objects.aggregate(Avg('B5'))
    B5_Avg = industry['B5__avg']

    B_avg = B1_Avg + B2_Avg + B3_Avg + B4_Avg + B5_Avg
    B_avg = B_avg / b_Element.objects.count()

    Avg_score = numpy.mean([A_avg, B_avg])

    context = {
            'A_score': A_avg,
            'B_score': B_avg,
            'Avg_score': Avg_score,
            }
    return render(request, "homepage.html", context)


def dashboard(request, farmer):

    industry = Farmer_a_score.objects.filter(farmerID=farmer)

    if not industry:
        context = {
            'farmer': farmer,
        }
        return render(request, "error.html", context)

    A_score = float(industry[0].A1) + float(industry[0].A2) + float(industry[0].A3) + float(industry[0].A4) + float(industry[0].A5)
    A_score = A_score / a_Element.objects.count()

    industry = Farmer_b_score.objects.filter(farmerID=farmer)
    if not industry:
        context = {
            'farmer': farmer,
        }
        return render(request, "error.html", context)

    B_score = float(industry[0].B1) + float(industry[0].B2) + float(industry[0].B3) + float(industry[0].B4) + float(industry[0].B5)
    B_score = B_score / b_Element.objects.count()

    Avg_score = numpy.mean([A_score, B_score])

    industry = Farmer.objects.filter(farmerID=farmer)
    if not industry:
        context = {
            'farmer': farmer,
        }
        return render(request, "error.html", context)

    farmer_name = industry[0].Name
    farmer_location = industry[0].Location
    farmer_region = industry[0].Region
    farmer_country = industry[0].Country

    context = {
            'A_score': A_score,
            'B_score': B_score,
            'Avg_score': Avg_score,
            'farmer_name': farmer_name,
            'farmer_location': farmer_location,
            'farmer_region': farmer_region,
            'farmer_country': farmer_country,
            }
    return render(request, "dashboard.html", context)
