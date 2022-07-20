from django.shortcuts import render
from .models import Vacancy

# Create your views here.

def home_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        filter_ = {}
        if city:
            filter_['city__name'] = city
        if language:
            filter_['language__name'] = language

        qs = Vacancy.objects.filter(**filter_)
    return render(request, 'home.html', {'object_list': qs})

