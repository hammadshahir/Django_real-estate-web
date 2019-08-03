from django.contrib import admin
from .models import Listing


#
class ListingAdmin(admin.ModelAdmin):
    # Display columns in admin
    list_display = ('id', 'title', 'city', 'price', 'realtor', 'list_date', 'is_published')
    # display links (click on id and title of property to see the details)
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city', 'zip_code', 'state',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
