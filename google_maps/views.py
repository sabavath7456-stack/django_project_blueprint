from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the google map app index.")

def home(request):
    return render(request, 'google_maps/home.html')