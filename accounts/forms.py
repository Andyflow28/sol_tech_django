from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    
    first_name = forms.CharField(
        required=True,
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre completo'
        })
    )
    
    class Meta:
        model = User
        fields = ("first_name", "username", "email", "password1", "password2")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'nombredeusuario'
        })
        self.fields['password1'].label = "Contraseña"
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Elige una contraseña segura'
        })
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Repite tu contraseña'
        })
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        return user