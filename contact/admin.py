from django.contrib import admin

from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone',
    ordering = 'id',
    search_fields = 'first_name',
    #list_filter = 'created_date',
