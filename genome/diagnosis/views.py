from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader
# from django.template import RequestContext

from diagnosis.models import Disease


def index(request):
    diseases = Disease.objects.order_by('disease_id')[:10]
    # template = loader.get_template('diagnosis/index.html')
    # context = RequestContext(request, {
    #     'diseases': diseases,
    # })
    # return HttpResponse(template.render(context))
    context = {
        'diseases': diseases,
    }
    return render(request, 'diagnosis/index.html', context)


def results(request, disease_id):
    response = "You're looking at the results of disease_id %s."
    return HttpResponse(response % disease_id)
