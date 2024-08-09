import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

    
#*REG-EXP -> 
"""
Flan que contenga los siguientes 
atributos:
● flan_uuid del tipo UUIDField
● name del tipo CharField (largo máximo 64 caracteres)
● description del tipo TextField
● image_url del tipo URLField
● slug del tipo SlugField
● is_private del tipo BooleanField
"""
# class ContactForm(models.Model):
#     pass
