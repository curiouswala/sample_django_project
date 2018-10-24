from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name):
   text = f"""<h1>Welcome {name} to my app !</h1>"""
   return HttpResponse(text)