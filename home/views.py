from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def rates(request):
    return render(request, 'home/rates.html')

def about(request):
    return render(request, 'home/about.html')

def blog(request):
    return render(request, 'home/blog.html')

def aaa(request):
    return render(request, 'home/aaa.html')