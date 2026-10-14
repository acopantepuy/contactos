from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['codigo', 'nombres', 'apellidos', 'rif', 'telefono_oficina', 'telefono_movil', 'correo']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'rif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'V-12345678-0'}),
            'telefono_oficina': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_movil': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }