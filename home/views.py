from django.shortcuts import render

# Create your views here.

def index(request):
    """ retruns the given request """ 
    return render(request, 'home/index.html')
