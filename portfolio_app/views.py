from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
# Render index.html
   return render( request, 'portfolio_app/index.html')

def stub(request):
   return render(request,"portfolio_app/stub.html")