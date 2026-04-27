from django import forms
from .models import Order

class OrderFrom(forms.ModelForm)
    class Meta:
       model = Order      
        fields = ['client', 'delivery_address', 'notes', 'status', 'total_price', 'delivery_mode']                 
        widgets = {
           'notes': forms.Textarea(attrs={'rows':6});
           'delivery_mode': forms.Select(attrs={'class': 'form-control'}),
       }

