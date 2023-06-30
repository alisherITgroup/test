from django.urls import path
from .views import *


urlpatterns = [
    path('post/', post_contact, name='post_contact'),
    path('get/', get_contacts, name='get_contacts')
]