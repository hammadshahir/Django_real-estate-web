from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .choices import bedroom_choices, bathroom_choices, price_choices, states_choices
from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id) #model, listing primary key

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    query_list = Listing.objects.order_by('-list_date')
    # Search by Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        # this if statement makes sure there is no empty string.
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)
        # Search by City
    if 'city' in request.GET:
        city = request.GET['city']
        # this if statement makes sure there is no empty string.
        if city:
            query_list = query_list.filter(city__iexact=city)

    # Search by State
    if 'state' in request.GET:
        state = request.GET['state']
        # this if-statement makes sure there is no empty string.
        if state:
            query_list = query_list.filter(state__iexact=state)

    # Search by bedroom
    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        # this if-statement makes sure there is no empty string.
        if bedroom:
            query_list = query_list.filter(bedroom__lte=bedroom) #lte = less than or equal to


        # Search by Max. Prices

    if 'price' in request.GET:
        price = request.GET['price']
        # this if-statement makes sure there is no empty string.
        if price:
            query_list = query_list.filter(price__lte=price)  # lte = less than or equal to

    context = {
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'price_choices': price_choices,
        'states_choices': states_choices,
        'listings': query_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
