from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	# return HttpResponse("About")
	return render(request,"home.html")

def about(request):
	# return HttpResponse("<h1> Home</h1>")
	return render(request,"about.html")