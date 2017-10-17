#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
   # return HttpResponse(u"hellow py!")
	return render(request,'home.html')

def add(request):
	a=request.GET['a']
	b=request.GET['b'] 
	c=int(a)+int(b)
	return HttpResponse(str(c)) #default ways

def add2(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))
