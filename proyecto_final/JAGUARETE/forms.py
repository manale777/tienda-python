from django import forms
from .models import Producto

class FormProducto(forms.ModelForm):
    
    #campos del modelo
    class Meta:
       model = Producto
       fields = ('titulo', 'imagen', 'descripcion', 'precio', 'categoria')