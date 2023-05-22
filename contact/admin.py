from django.contrib import admin

from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'show',
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name'
    #list_editable = 'first_name', 'last_name', 'show',
    #list_filter = 'created_date',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
    
