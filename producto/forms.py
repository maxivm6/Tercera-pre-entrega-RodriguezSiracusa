from django import forms

class FormProducto(forms.Form):
  
    nombre = forms.CharField(max_length=40, required=True,widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), label=False)
    descripcion = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Descripcion'}), label=False)
    precio = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Precio'}), label=False)
    stock = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Stock'}), label=False)
    
    