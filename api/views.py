from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact


@api_view(http_method_names=['POST', 'GET'])
def post_contact(request):
    if request.method == "POST":
        data = request.data
        fullname = data['fullname']
        phone = data['phone']
        direction = data['direction']
        contact = Contact(
            fullname=fullname,
            phone=phone,
            direction=direction
        )
        contact.save()
        print(
            fullname,
            phone,
            direction
        )
        return Response({
            "status": "ok",
            "info": "Your data saved.",
        })

@api_view(http_method_names=['GET'])
def get_contacts(request):
    queryset = Contact.objects.all()
    contacts = {}
    counter = 1
    for contact in queryset:
        contacts[f'{counter}'] = {
            'fullname': contact.fullname,
            'phone': contact.phone,
            'direction': contact.direction
        }
        counter += 1
    return Response(contacts)