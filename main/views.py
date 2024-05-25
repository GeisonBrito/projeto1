from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
def index(request):
   
    return render(request,'main/index.html')

def show(request, id):
    return render(request,'main/show.html')