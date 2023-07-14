from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.core.paginator import Paginator
from .forms import ContactForm
from utils.handle_upload_image import handle_uploaded_file
from datetime import datetime
from .utils.initial_data_form import set_initial_data
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def index(request,page=1):    
    contacts = Contact.objects.all()
    paginator = Paginator(contacts,10)
    deleted=False
    try:
        deleted = request.GET["contact"]
    except:
        ...
    if deleted==False:
        context = {
            'contacts':paginator.page(page),
            'paginator':paginator
        }
    else:
        context = {
            'contacts':paginator.page(page),
            'paginator':paginator,
            'message':"Contato deletado com sucesso"
        }
    return render(request,'contacts/index.html',context)

def search_contact(request):
    nome = request.GET.get("name")
    page = int(request.GET.get("page"))
    contacts = Contact.objects.filter(Q(primeiro_nome__icontains=nome)|Q(ultimo_nome__icontains=nome))
    paginator = Paginator(contacts,10)
    return render(request,'contacts/search.html',{
        'contacts':paginator.page(page),
        'paginator':paginator,
        'name':nome

    })


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
    
def delete_contact_view(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    delete = False
    try:
        delete = request.GET['delete']
    except:
        ...
    if delete == False:
        return render(request,'contacts/view_contact.html',{
            "show_exclude":True,
            "contact":contact
        })
    else:
        contact.delete()
        base_url = reverse('contact:index')
        query="contact=deleted"
        url = f"{base_url}?{query}"
        return redirect(url)
