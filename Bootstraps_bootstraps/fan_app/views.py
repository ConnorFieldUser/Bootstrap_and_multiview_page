from django.shortcuts import render

# Create your views here.
from fan_app.models import Instructor


def index_view(request):
    context = {
        "start": "start"
    }
    return render(request, 'index.html', context)
