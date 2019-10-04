from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "blog.html", {})
    #return HttpResponse("<h1>This is the homepage, welcome to the project men</h1>")
