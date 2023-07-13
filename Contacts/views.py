from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.core.paginator import Paginator
from .forms import ContactForm
from utils.handle_upload_image import handle_uploaded_file
from datetime import datetime
from .utils.initial_data_form import set_initial_data

# Create your views here.
def index(request,page=1):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts,10)
    context = {
        'contacts':paginator.page(page),
        'paginator':paginator
    }
    return render(request,'contacts/index.html',context)

def view_contact(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    return render(request,'contacts/view_contact.html',{
        'contact':contact,
    })
 
def edit_contact(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    try:
        dados_iniciais={
            'primeiro_nome':contact.primeiro_nome,
            'ultimo_nome':contact.ultimo_nome,
            'email':contact.email,
            'celular':contact.celular,
            'description':contact.description,
            'picture':contact.picture.url

        }
    except:
        dados_iniciais={
            'primeiro_nome':contact.primeiro_nome,
            'ultimo_nome':contact.ultimo_nome,
            'email':contact.email,
            'celular':contact.celular,
            'description':contact.description,
        }
    if request.method == "POST":
        form = ContactForm(request.POST,request.FILES,instance=contact)
        
        if form.is_valid():
            contact=form.save(commit=False)
            contact.save()
            form = ContactForm(initial=set_initial_data(contact))
            return render(request,'contacts/edit_contact.html',
            {
                'message':"Contato editado com sucesso",
                'form':form,
                'contact_picture_url':contact.picture,
                'contact_id':contact.pk
            })
        else:
            return render(request,'contacts/edit_contact.html',
            {
                'message':"Corrija o erros",
                'form':form,
                'contact_picture_url':contact.picture,
                'contact_id':contact.pk
            })
    else:
        form = ContactForm(initial=dados_iniciais)
        return render(request,'contacts/edit_contact.html',{
            'form':form,
            'contact_picture_url':contact.picture,
            'contact_id':contact.pk
        })
    
def create_contact(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST,request.FILES)
        
        if form.is_valid():
            contact=form.save(commit=False)
            contact.save()
            form = ContactForm(initial=set_initial_data(contact))
            return render(request,'contacts/create_contact.html',
            {
                'message':"Contato editado com sucesso",
                'form':form,
                'contact_picture_url':contact.picture,
            })
        else:
            return render(request,'contacts/create_contact.html',
            {
                'message':"Corrija o erros",
                'form':form,
            })
    else:
        form = ContactForm()
        return render(request,'contacts/create_contact.html',{
            'form':form,
        })
