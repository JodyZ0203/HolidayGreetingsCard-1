from django.urls import path
from .views import CardInfoView

urlpatterns = [
    path('', CardInfoView.as_view()),
    #path('planner', main)
]
