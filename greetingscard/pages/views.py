from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card.models import CardInfo
from card.forms import CardFields
# Create your views here.

'''
def myView(request):
    greet_settings = CardInfo.objects.all()
    print(greet_settings)
    return render(request, 'index.html',
    {'all_items': greet_settings})
'''
def myView(request):
    form = CardFields(request.POST or None)

    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        form = CardFields()

        if request.method == 'POST':
            return redirect('/results')
    
    context = {
        'form' : form
    }
    return render(request, 'index.html', context)

def results(request, id=1):
    picture = get_object_or_404(CardInfo, pk=id)
    #picture = get_object_or_404(CardInfo, id=id)
    return render(request, 'card/results.html', {'picture': picture})