from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, bathroom_choices, price_choices, states_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'price_choices': price_choices,
        'states_choices': states_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors

    realtors = Realtor.objects.order_by('-hired_date')

    # Get MVP

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors_available': mvp_realtors
    }

    return render(request, 'pages/about.html', context)