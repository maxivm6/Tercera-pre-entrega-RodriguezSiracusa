from django import forms

class FormEmpleado(forms.Form):
    
    nombre = forms.CharField(max_length=20, required=True,widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), label=False)
    apellido = forms.CharField(max_length=20, required=True,widget=forms.TextInput(attrs={'placeholder': 'Apellido'}), label=False)
    salario = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Salario'}), label=False)
    area = forms.CharField(max_length=60, required=True,widget=forms.TextInput(attrs={'placeholder': 'Area'}), label=False)