from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from card.models import CardInfo
# Create your views here.

def myView(request):
    greet_settings = CardInfo.objects.all()
    print(greet_settings)
    return render(request, 'index.html',
    {'all_items': greet_settings})

def results(request, id):
    picture = get_object_or_404(CardInfo, pk=id)
    return render(request, 'card/results.html', {'picture': picture})