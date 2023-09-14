from django.shortcuts import render, HttpResponse

# Create your views here.

# def Index(request):
#     return HttpResponse("It is working")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def school_admin(request):
    return render(request, 'schoolgallery.html')    
