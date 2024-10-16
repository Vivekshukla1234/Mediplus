from django.shortcuts import render

# Create your views here.

def view_home(request):
    resp=render(request,'hms/home.html')
    return resp

def view_doctos(request):
    resp=render(request,'hms/doctos.html')
    return resp

def veiw_services(request):
    resp=render(request,'hms/services.html')
    return resp