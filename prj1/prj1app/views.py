from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'people':obj1})

# Create your views here.
#def operations(request):
    #x = int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #sum = x+y
    #diff = x-y
    #prod=x*y
    #div=x/y
    #return render(request,"result.html",{'sumresult':sum,'subtraction':diff,'multi':prod,'division':div})
