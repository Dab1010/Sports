from django.urls import path
from . import views

urlpatterns = [
    path('sports/', views.sport_list, name='sport-list'),
    path('sports/<int:id>/', views.sport_detail, name='sport-detail'),
]
