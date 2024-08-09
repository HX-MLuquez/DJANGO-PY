from django.core.management.base import BaseCommand
# from web.forms import ContactFormForm, ContactModelForm

class Command(BaseCommand):
    help = 'Test form creation and validation'

    def handle(self, *args, **options):
        self.function_test_form()

    def function_test_form(self):  
       pass

#* ContactForm.objects.create(**form.cleaned_data) <- sintaxis simple y adecuada para crear en la db

#!IMPORTANTE al momento de crear en la db con la data que nos llega
#* Sin uso de **, debemos descomponer del diccionario todos los atributos cual argumentos:
"""
contact_form = ContactForm.objects.create(
    name=form.cleaned_data['name'],
    email=form.cleaned_data['email'],
    message=form.cleaned_data['message']
)
"""

