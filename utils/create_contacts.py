import subprocess
import ipsum
from random import randint
#from Contacts.models import Contact
import sys
from pathlib import Path
import os
import django

def generate_phone_number():
    DDDs = [
            61,62,64,65,66,67,82,71,73,74,75,77,85,88,98,99,
            83,81,87,86,89,84,79,68,96,92,97,91,93,94,85,88,
            98,99,83,81,87,86,89,84,79,68,96,92,97,91,93,94,
            69,95,63,27,28,31,32,33,34,35,37,38,21,22,24,11,
            12,13,14,15,16,17,18,19,41,42,43,44,45,46,51,53,
            54,55,47,48,49
            ]
    result = f"({DDDs[randint(0,len(DDDs)-1)]}){randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"

    return result

NUMBER_OF_OBJECTS = 1000
model = ipsum.load_model("en")

DJANGO_BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'MeusContatos.settings'

django.setup()
from Contacts.models import Contact
Contact.objects.all().delete()
for n in range(NUMBER_OF_OBJECTS):
    try:
        description_text = model.generate_paragraphs(randint(1,3))[0]
        with open('utils/names.txt','r') as file:
            texto = file.read()
            texto=texto.strip().split("#")
            H_M = randint(0,1)
            all_names = texto[H_M]
            all_names = all_names.split('\n')
            first_name = all_names[randint(0,len(all_names)-1)].strip()
            last_name = all_names[randint(0,len(all_names)-1)].strip()
            while last_name == first_name:
                last_name = all_names[randint(0,len(all_names)-1)].strip()
            email = str(f"{first_name.replace(' ','')}{last_name.replace(' ','')}@email.com").lower()
            #show =  True if randint(0,1) == 1 else False
            show = True
            phone = generate_phone_number()
            contact = Contact()
            contact.primeiro_nome = first_name
            contact.ultimo_nome = last_name
            contact.email = email
            contact.celular = phone
            contact.description = description_text
            contact.save()
    except:
        ...
    #contato=models.Contact(primeiro_nome="teste",ultimo_nome="zé")
    #print(contato.primeiro_nome,contato.ultimo_nome)


