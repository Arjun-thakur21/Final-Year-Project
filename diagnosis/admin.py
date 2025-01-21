from django.contrib import admin
from diagnosis.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(Contact,ContactAdmin)
# Register your models here.
