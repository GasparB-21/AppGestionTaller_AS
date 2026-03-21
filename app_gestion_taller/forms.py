from django import forms
from .models import Cliente, Coche, Servicio, Reparacion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = '__all__'