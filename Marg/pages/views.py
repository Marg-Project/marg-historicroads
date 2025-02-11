from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request , 'pages/index.html')

def about(request):
    return render(request , 'pages/about.html')

def explore(request):
    return render(request , 'pages/explore.html')

def identification_documentation(request):
    return render(request , 'pages/identification.html')

def conservation(request):
    return render(request , 'pages/conservation.html')

def management(request):
    return render(request , 'pages/management.html')

def network(request):
    return render(request , 'pages/network.html')