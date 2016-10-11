from django.shortcuts import render

# Create your views here.
from fan_app.models import Instructor


def index_view(request):
    context = {
    }
    return render(request, "index.html", context)


def joels_info_view(request):
    context = {
        "joel": Instructor.objects.get(firstname="Joel")
    }
    return render(request, "joels_info.html", context)


def my_info_view(request):
    context = {
    }
    return render(request, "my_info.html", context)


def about_view(request):
    context = {
    }
    return render(request, "about.html", context)
