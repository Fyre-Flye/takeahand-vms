from django.shortcuts import render

# Create your views here.
def home(resquest):
    return render(resquest, 'index.html')
