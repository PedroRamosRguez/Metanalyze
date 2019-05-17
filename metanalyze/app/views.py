
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AlgorithmForm

def index(request):
    form = AlgorithmForm()
    return render(
        request,
        'app/index.html',{'form': form}
    )

def about(request):
    return render(request,'app/about.html')

