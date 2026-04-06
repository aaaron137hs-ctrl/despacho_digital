from django import forms
from .models import Caso

class CasoForm(forms.ModelForm):
    class Meta:
        model = Caso
        fields = ['titulo', 'cliente', 'descripcion']
        # Esto le pone clases de Bootstrap a los cuadritos de texto
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }