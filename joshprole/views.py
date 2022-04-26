from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('joshprole/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
def invoices(request):
    template = loader.get_template('dummy/invoices.html')
    context = {}
    return HttpResponse(template.render(context, request))