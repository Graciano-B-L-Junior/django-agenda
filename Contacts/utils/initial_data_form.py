from ..models import Contact

def set_initial_data(contact:Contact):
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
    return dados_iniciais