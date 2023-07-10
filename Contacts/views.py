from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.core.paginator import Paginator
from .forms import ContactForm

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
        'contact':contact
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
        form = ContactForm(request.POST)

        if form.is_valid():
            contact.primeiro_nome = form.primeiro_nome
            contact.ultimo_nome = form.ultimo_nome
            contact.description = form.description
            contact.celular = form.celular
            contact.picture = form.picture
            return render(request,'contacts/edit_contact.html',
                            {
                'message':"Contato criado com sucesso",
                'form':form
            })
        else:
            return render(request,'contacts/edit_contact.html',
            {
                'message':"Corrija o erros",
                'form':form
            })
    else:
        form = ContactForm(initial=dados_iniciais)
        return render(request,'contacts/edit_contact.html',{
            'form':form
        })