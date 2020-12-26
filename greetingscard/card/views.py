from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CardInfoSerializer
from .models import CardInfo
from rest_framework.views import APIView
from rest_framework.response import Response
#from django.http import HttpResponse

# Create your views here.
#def main(request):
 #   return HttpResponse("This is a degree Planner")

class CardInfoView(generics.CreateAPIView):
    queryset = CardInfo.objects.all()
    serializer_class = CardInfoSerializer