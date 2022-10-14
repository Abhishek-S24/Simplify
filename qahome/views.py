from difflib import context_diff
from django.shortcuts import render,HttpResponse
from qahome.models import Data

# View for index
def index(request):
    version =  Data.objects.all().order_by('version')[::-1]  #ordering in order to reflect new changes first 
    return render(request, 'newindex.html',{'version': version})
