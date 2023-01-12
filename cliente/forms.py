from django import forms

class FormCliente(forms.Form):
    
    nombre = forms.CharField(max_length=20, required=True,widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), label=False)
    apellido = forms.CharField(max_length=20, required=True,widget=forms.TextInput(attrs={'placeholder': 'Apellido'}), label=False)
    email = forms.EmailField(max_length=45, required=True,widget=forms.TextInput(attrs={'placeholder': 'Email'}), label=False)
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Telefono'}), label=False)
    direccion = forms.CharField(max_length=60, required=True,widget=forms.TextInput(attrs={'placeholder': 'Direccion'}), label=False)
    