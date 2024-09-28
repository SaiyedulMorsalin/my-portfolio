from django.shortcuts import render


# Create your views here.
def home_page(request):
    context = {"greeting": "Welcome to the homepage!"}
    return render(request, "index.html", context)
