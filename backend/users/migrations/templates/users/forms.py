from django import forms
from .models import Order

class OrderFrom(forms.ModelForm)
    class Meta:
       model = Order
        fields = ['client', 'delivery_address', 'notes', 'status']
       widgets = {
           'notes': forms.Textarea(attrs={'rows':6});
      }
