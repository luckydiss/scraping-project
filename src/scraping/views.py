from django.shortcuts import render
from .models import Vacancy
from scraping.forms import FindForm

# Create your views here.

def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        filter_ = {}
        if city:
            filter_['city__slug'] = city
        if language:
            filter_['language__slug'] = language

        qs = Vacancy.objects.filter(**filter_)
    return render(request, 'home.html', {'object_list': qs,
                                         'form': form})

