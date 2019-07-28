# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .models import Article
# Create your views here.

def article_list(request):
	articles=Article.objects.all().order_by("date")
	return render(request,"list.html",{"articles":articles})
	# return HttpResponse("PREM")

def article_detail(request,slug):
	# return HttpResponse(slug)
	article=Article.objects.get(slug=slug)
	return render(request,'articles/article_details.html',{'article':article})