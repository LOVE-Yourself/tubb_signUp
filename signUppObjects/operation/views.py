from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class KitecarView(View):
    def get(self,request):
        return render(request,'kitcar.html')

class LoadAppView(View):
    def get(self,request):
        return render(request,'app.html')

class AboutView(View):
    def get(self,request):
        return render(request,'about.html')

class JoinUsVIew(View):
    def get(self,request):
        return render(request,'join.html')
