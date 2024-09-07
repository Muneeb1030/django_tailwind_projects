from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request=request, template_name='mini_templates/home.html')

def mini_1(request):
    return render(request=request, template_name='mini_templates/mini_1.html')

def mini_2(request):
    return render(request=request, template_name='mini_templates/mini_2.html')

def mini_3(request):
    return render(request=request, template_name='mini_templates/mini_3.html')

def mini_4(request):
    return render(request=request, template_name='mini_templates/mini_4.html')

def mini_5(request):
    return render(request=request, template_name='mini_templates/mini_5.html')

def project_1(request):
    return render(request=request, template_name='projects/project_1.html')

def project_2(request):
    return render(request=request, template_name='projects/project_2.html')

def project_3(request):
    return render(request=request, template_name='projects/project_3.html')

def project_4(request):
    return render(request=request, template_name='projects/project_4.html')

def project_5(request):
    return render(request=request, template_name='projects/project_5.html')
