from django.db import models
from tinymce.models import HTMLField




# Data database model.
class Data(models.Model):
    version = models.CharField(max_length= 100)
    release_title = models.CharField(max_length =100)
    content = HTMLField()
    
    
    def __str__(self):
        return self.version