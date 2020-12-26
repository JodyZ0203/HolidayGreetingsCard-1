from django.shortcuts import render
from django.http import HttpResponse
from card.models import CardInfo
# Create your views here.

def myView(request):
    greet_settings = CardInfo.objects.all()
    print(greet_settings)
    return render(request, 'index.html',
    {'all_items': greet_settings})