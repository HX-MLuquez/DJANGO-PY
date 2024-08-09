import uuid
from django.db import models
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    
"""
class ContactForm(models.Model): 
● contact_form_uuid del tipo UUIDField, con valor por defecto uuid.uuid4, no 
editable
● customer_email del tipo EmailField
● customer_name del tipo CharField (largo máximo 64 caracteres)
● message del tipo TextField

contact_form_uuid = models.UUIDField(default=uuid.uuid4)
"""

