from django.shortcuts import render
from rest_framework import generics
from .serializers import CardInfoSerializer
from .models import CardInfo
#from django.http import HttpResponse

# Create your views here.
#def main(request):
 #   return HttpResponse("This is a degree Planner")

class CardInfoView(generics.CreateAPIView):
    queryset = CardInfo.objects.all()
    serializer_class = CardInfoSerializer