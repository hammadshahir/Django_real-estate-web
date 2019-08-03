from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'realtor_name', 'realtor_email',)
    list_display_links = ('id', 'realtor_name',)
    search_fields = ('realtor_name', 'realtor_email',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
