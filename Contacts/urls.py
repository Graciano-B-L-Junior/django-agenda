
from django.urls import path
from . import views


app_name = 'contact'

urlpatterns = [
    path('',views.index,name='index'),
    path('search_page=<int:page>',views.index,name='index'),
    path('contact/<int:contact_id>',views.view_contact,name='view_contact'),
    path('contact/edit_contact/<int:contact_id>',views.edit_contact,name='edit_contact'),
    path('contact/create_contact',views.create_contact,name='create_contact'),
    path('contact/delete_contact/<int:contact_id>',views.delete_contact_view,name='delete_contact'),
]
