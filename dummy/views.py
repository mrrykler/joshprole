from django.shortcuts import render

# Create your views here.

def invoices(request):
    template = loader.get_template('dummy/invoices.html')
    context = {}
    return HttpResponse(template.render(context, request))