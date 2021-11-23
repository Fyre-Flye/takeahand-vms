from django.forms import ModelForm
from ERP.models import Voluntarios

# Create the form class.
class VoluntariosForm(ModelForm):
     class Meta:
         model = Voluntarios
         fields = ['nome', 'sobrenome', 'email', 'cpf', 'funcao','bairro','telefone', 'horas_semanais', 'horas_contribuidas']
