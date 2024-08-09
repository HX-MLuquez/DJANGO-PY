from django.contrib import admin

from .models import Flan, ContactForm

admin.site.register(ContactForm)
admin.site.register(Flan)

