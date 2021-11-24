from django.shortcuts import redirect, render
from ERP.forms import VoluntariosForm
from ERP.models import Voluntarios
from django.views.generic import TemplateView

def home(request):
    return render(request, 'index.html')

def crud(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Voluntarios.objects.filter(nome__icontains=search)
    else:
        data['db'] = Voluntarios.objects.all()

    return render(request, 'crud.html', data)


def form(request):
    data = {}
    data['form'] = VoluntariosForm()
    return render(request, 'form.html', data)


def create(resquest):
    form = VoluntariosForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crud')


def view(request, pk):
    data = {}
    data['db'] = Voluntarios.objects.get(pk=pk)
    return render(request,'view.html', data)


def edit(request, pk):
    data={}
    data['db'] = Voluntarios.objects.get(pk=pk)
    data['form'] = VoluntariosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Voluntarios.objects.get(pk=pk)
    form = VoluntariosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('crud')


def delete (request, pk):
    db = Voluntarios.objects.get(pk=pk)
    db.delete()
    return redirect ('crud')

class HomePageView(TemplateView):
    template_name = 'index.html'