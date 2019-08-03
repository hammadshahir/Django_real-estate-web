from django.shortcuts import render, HttpResponse, redirect
from .models import Contacts
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        contact = Contacts(listing = listing, listing_id = listing_id, name = name, email = email,
                           phone = phone, message = message, user_id = user_id)
        contact.save()

        messages.success(request, 'Thank you, we will come back to you soon!')
        return redirect('/listings'+listing_id)