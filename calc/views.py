from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html',{'name': 'Atharva'})


def add(request):
    var1= int(request.POST["num1"])
    var2= int(request.POST["num2"])
    res= var1 + var2
    return render(request, 'result.html', {'result': res})