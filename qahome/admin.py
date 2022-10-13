from django.contrib import admin
from .models import Data

# Register your models here.
admin.site.site_title = "Welcome to Simplify QA Admin"
admin.site.site_header = 'SimplifyQA Admin'
admin.site.register(Data)