from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/HomePage.html')
# Create your views here.
