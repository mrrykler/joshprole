from django.http import HttpResponse
from django.template import loader
from dummy.models import *

def index(request):
    template = loader.get_template('joshprole/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
