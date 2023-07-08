from django import forms

class ContactForm(forms.Form):
    primeiro_nome = forms.CharField(label="Primeiro nome",max_length="50",required=True)
    ultimo_nome = forms.CharField(label="Ultimo nome",max_length="50",required=True)
    email = forms.EmailField(label="email",required=True)
    celular = forms.CharField(label="Celular",max_length="11",required=True)
    picture = forms.ImageField(required=False)
