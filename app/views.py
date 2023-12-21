from django.shortcuts import render
from app.models import *
# Create your views here.

def dept(request):
    QLDO = Dept.objects.all()

    d={'dept' : QLDO}
    

    return render(request, 'dept.html', context=d)



def emp(request):
    QLEO= Emp.objects.all()

    d={'emp' : QLEO}

    return render(request, 'emp.html', context=d)