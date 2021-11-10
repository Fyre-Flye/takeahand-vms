from django.shortcuts import redirect, render
from ERP.forms import VoluntariosForm
from ERP.models import Voluntarios 
# Create your views here.
def home(resquest):
    data={}
    data['db'] = Voluntarios.objects.all()
    return render(resquest, 'index.html', data)

def form(resquest):
    data = {}
    data['form'] = VoluntariosForm()
    return render(resquest, 'form.html', data)

def create(resquest):
    form = VoluntariosForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Voluntarios.objects.get(pk=pk)
    return render(request,'view.html', data)