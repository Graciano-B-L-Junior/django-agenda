from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("primeiro_nome","ultimo_nome","email","celular","description","picture")
