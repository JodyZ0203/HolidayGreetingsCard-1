from django.urls import path
from .views import CardInfoView
from pages import views

app_name = 'card'
urlpatterns = [
    path('', CardInfoView.as_view()),
    path('<int:id>/results/', views.results, name='results'),
    #path('planner', main)
]
