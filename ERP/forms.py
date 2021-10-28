from django.forms import ModelForm
from ERP.models import Voluntarios

# Create the form class.
class VoluntariosForm(ModelForm):
     class Meta:
         model = Voluntarios
         fields = ['nome', 'funcao', 'numero_de_id']
