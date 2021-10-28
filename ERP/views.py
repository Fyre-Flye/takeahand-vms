from django.shortcuts import render
from ERP.forms import VoluntariosForm

# Create your views here.
def home(resquest):
    return render(resquest, 'index.html')

def form(resquest):
    data = {}
    data['form'] = VoluntariosForm()
    return render(resquest, 'form.html', data)
