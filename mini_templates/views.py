from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request=request, template_name='mini_templates/home.html')

def mini_1(request):
    return render(request=request, template_name='mini_templates/mini_1.html')